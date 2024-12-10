with open("input.txt") as f:
    field = [ list(line) for line in f.read().split("\n") ]

    starts = [(j, i) for i, row in enumerate(field) for j, x in enumerate(row) if x == "0"]

    def find_paths(field, value, pos, prev_path):
        if value == 9:
            return [prev_path]

        neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        neighbors_in_field = [n for n in neighbors if 0 <= n[0] < len(field[0]) and 0 <= n[1] < len(field)]
        paths = []
        for neighbor in neighbors_in_field:
            if field[neighbor[1]][neighbor[0]] == str(value + 1):
                paths.extend(find_paths(field, value + 1, neighbor, prev_path + [neighbor]))
        return paths

    complete_paths = list()
    for start in starts:
        complete_paths += (find_paths(field, 0, start, [start]))

    # Take set of first and last pairs
    pairs = set((path[0], path[-1]) for path in complete_paths)
    print(len(pairs))

    # Part 2
    print(len(complete_paths))
