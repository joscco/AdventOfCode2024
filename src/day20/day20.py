from heapq import heappush, heappop


def find_path(grid, start, end):
    visited = set()
    queue = [(0, start)]
    path = [start]

    while True:
        steps, pos = heappop(queue)
        for dir in dirs:
            forward_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if (forward_pos[0] < 0 or forward_pos[0] >= len(grid[0])
                    or forward_pos[1] < 0 or forward_pos[1] >= len(grid)):
                continue
            if forward_pos in visited or grid[forward_pos[1]][forward_pos[0]] in ["#", "S"]:
                continue
            path.append(forward_pos)
            visited.add(forward_pos)
            if forward_pos == end:
                return path
            heappush(queue, (steps + 1, forward_pos))


with open('input.txt') as f:
    maze = [list(l.strip()) for l in f]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i, l in enumerate(maze):
        for j, c in enumerate(l):
            if c == "S":
                start = (j, i)
            elif c == "E":
                end = (j, i)

    initial_path = find_path(maze, start, end)
    cheats_count_with_min_distance = 0
    cheats_count_with_max_distance = 0

    min_steps_to_save = 100
    max_shortcut_distance = 20

    # Since there is only ONE normal path, every cheat is a shortcut between two positions on the path
    for index, position in enumerate(initial_path):
        for shortcut_index in range(index + min_steps_to_save, len(initial_path)):
            shortcut_end = initial_path[shortcut_index]
            index_difference = shortcut_index - index
            space_distance = abs(position[0] - shortcut_end[0]) + abs(position[1] - shortcut_end[1])
            if space_distance > max_shortcut_distance:
                # Shortcut would be too long
                continue
            steps_gained = index_difference - space_distance
            if steps_gained < min_steps_to_save:
                # Not interesting
                continue
            cheats_count_with_max_distance += 1
            if space_distance <= 2:
                cheats_count_with_min_distance += 1

    # Part 1
    print("Part 1:", cheats_count_with_min_distance)

    # Part 2
    print("Part 2:", cheats_count_with_max_distance)
