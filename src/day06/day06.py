with open("input.txt") as f:
    field = [list(line) for line in f.read().split("\n")]
    start = next((j, i) for i, row in enumerate(field) for j, x in enumerate(row) if x == "^")
    obstructions = set((j, i) for i, row in enumerate(field) for j, x in enumerate(row) if x == "#")
    directions = [(0, -1), (1, 0), (0,1), (-1, 0)]

    current_position_1 = start
    current_direction_1 = (0, -1)

    visited_positions = set()
    while 0 <= current_position_1[1] < len(field) and 0 <= current_position_1[0] < len(field[0]):
        visited_positions.add(current_position_1)
        next_position_1 = (current_position_1[0] + current_direction_1[0], current_position_1[1] + current_direction_1[1])
        while next_position_1 in obstructions:
            current_direction_1 = directions[(directions.index(current_direction_1) + 1) % len(directions)]
            next_position_1 = (current_position_1[0] + current_direction_1[0], current_position_1[1] + current_direction_1[1])
        current_position_1 = next_position_1

    print(len(visited_positions))

    # Part 2

    def has_loop(obstruction_set, new):
        visited_with_directions = set()
        current_position = start
        current_direction = (0, -1)
        while 0 <= current_position[1] < len(field) and 0 <= current_position[0] < len(field[0]):
            if (current_position, current_direction) in visited_with_directions:
                return True
            visited_with_directions.add((current_position, current_direction))
            next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
            while next_position == new or next_position in obstruction_set:
                current_direction = directions[(directions.index(current_direction) + 1) % len(directions)]
                next_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
            current_position = next_position
        return False


    obstacle_positions_causing_loops = 0

    for (i, j) in visited_positions:
            if has_loop(obstructions, (i, j)):
                obstacle_positions_causing_loops += 1

    print(obstacle_positions_causing_loops)

