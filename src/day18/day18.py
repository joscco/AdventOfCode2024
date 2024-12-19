def find_shortest_path(grid):
    grid_dim = len(grid)
    visited = set()
    queue = [(0, 0, 0)]
    while queue:
        x, y, steps = queue.pop(0)
        if x < 0 or x >= grid_dim or y < 0 or y >= grid_dim or (x, y) in visited or grid[y][x] == "#":
            continue
        if (x, y) == (grid_dim - 1, grid_dim - 1):
            return steps
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            queue.append((x + dx, y + dy, steps + 1))
    else:
        return -1


with open('input.txt') as f:
    positions = list([d.split(",") for d in f.read().split("\n")])
    positions = [(int(x), int(y)) for x, y in positions]

    grid_dim = 71
    number_of_positions = 1024
    grid = [["." for _ in range(grid_dim)] for _ in range(grid_dim)]
    for i, (x, y) in enumerate(positions):
        if i < number_of_positions:
            grid[y][x] = "#"

    print(find_shortest_path(grid))

    # Part 2
    grid = [["." for _ in range(grid_dim)] for _ in range(grid_dim)]

    for i, (x, y) in enumerate(positions):
        grid[y][x] = "#"
        if find_shortest_path(grid) == -1:
            print(x, y)
            break

