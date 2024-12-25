with open("input.txt") as f:
    data_sets = f.read().strip().split("\n\n")

def parse_lock(grid):
    return [sum(row[column] == "#" for row in grid[1:]) for column in range(len(grid[0]))]

def parse_key(grid):
    return [sum(row[column] == "#" for row in grid[:-1]) for column in range(len(grid[0]))]

locks = [parse_lock(data.split("\n")) for data in data_sets if data.startswith("#")]
keys = [parse_key(data.split("\n")) for data in data_sets if not data.startswith("#")]

fitting_combinations = sum(all(lock[i] + key[i] <= 5 for i in range(5)) for lock in locks for key in keys)
print(fitting_combinations)