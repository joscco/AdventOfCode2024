with open("input.txt") as f:
    field = [list(line) for line in f.read().split("\n")]

    def find_paths(field, value, pos, prev_path):
        if value == 9:
            return [prev_path]

        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = [(pos[0] + dx, pos[1] + dy) for dx, dy in offsets]
        valid_neighbors = [n for n in neighbors if 0 <= n[0] < len(field[0]) and 0 <= n[1] < len(field)]
        paths = []
        for neighbor in valid_neighbors:
            if field[neighbor[1]][neighbor[0]] == str(value + 1):
                paths.extend(find_paths(field, value + 1, neighbor, prev_path + [neighbor]))
        return paths

    starts = [(j, i) for i, row in enumerate(field) for j, x in enumerate(row) if x == "0"]
    complete_paths = [path for start in starts for path in find_paths(field, 0, start, [start])]

    # Take set of first and last pairs
    pairs = {(path[0], path[-1]) for path in complete_paths}
    print(len(pairs))

    # Part 2
    print(len(complete_paths))