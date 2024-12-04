with open("input.txt") as f:
    s = [list(line) for line in f.read().split("\n")]

    def find_in_direction(grid, pos, rest, direction):
        for i in range(0, len(rest)):
            next_pos = (pos[0] + i * direction[0], pos[1] + i * direction[1])
            if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][next_pos[1]] == rest[i]):
                return False
        return True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total_sum = 0
    for i, row in enumerate(s):
        for j, x in enumerate(row):
            for d in directions:
                if find_in_direction(s, (i, j), "XMAS", d):
                    total_sum += 1
    print(total_sum)

    def find_cross_s_and_m(grid, pos, rel_pos_1, rel_pos_2):
        pos_1 = (pos[0] + rel_pos_1[0], pos[1] + rel_pos_1[1])
        pos_2 = (pos[0] + rel_pos_2[0], pos[1] + rel_pos_2[1])
        return all(0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0]) for p in [pos_1, pos_2]) and \
               ((grid[pos_1[0]][pos_1[1]], grid[pos_2[0]][pos_2[1]]) in [('S', 'M'), ('M', 'S')])

    total_sum = sum(find_cross_s_and_m(s, (i, j), (-1, 1), (1, -1)) and find_cross_s_and_m(s, (i, j), (-1, -1), (1, 1)) for i, row in enumerate(s) for j, x in enumerate(row) if x == 'A')
    print(total_sum)