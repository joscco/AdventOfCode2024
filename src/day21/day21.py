from functools import cache

@cache
def find_cheapest_dir_path_from_to(from_x, from_y, to_x, to_y, robot_levels, avoid):
    best_path_length = None
    todo = [(from_x, from_y, "")]

    while len(todo) > 0:
        from_x, from_y, path = todo.pop(0)
        if (from_x, from_y) == (to_x, to_y):
            best_path_length = min_without_nones(best_path_length, find_cheapest_path_translation(path + "A", robot_levels - 1))
        elif (from_x, from_y) != avoid:
            for dx, dy, key in ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")):
                if is_fitting_direction(from_x, to_x, dx) or is_fitting_direction(from_y, to_y, dy):
                    todo.append((from_x + dx, from_y + dy, path + key))

    return best_path_length

@cache
def find_cheapest_path_translation(path, robot_levels):
    if robot_levels == 1:
        return len(path)

    best_path_length = 0
    pad = decode_pad("x^A<v>", 3)
    x, y = pad["A"]

    for key in path:
        to_x, to_y = pad[key]
        best_path_length += find_cheapest_dir_path_from_to(x, y, to_x, to_y, robot_levels, pad["x"])
        x, y = to_x, to_y

    return best_path_length

def min_without_nones(best_recent_path, best_cached_path):
    vals = [x for x in [best_recent_path, best_cached_path] if x is not None]
    return min(vals)

def decode_pad(val, width):
    return {val: (x % width, x // width) for x, val in enumerate(val)}

def is_fitting_direction(start, dest, change):
    return (change < 0 and dest < start) or (change > 0 and dest > start)

def calculate_score(codes, robots):
    total_score = 0
    pad = decode_pad("789456123x0A", 3)
    for code in codes:
        code_score = 0
        x, y = pad["A"]
        for val in code:
            to_x, to_y = pad[val]
            code_score += find_cheapest_dir_path_from_to(x, y, to_x, to_y, robots, pad["x"])
            x, y = to_x, to_y
        total_score += code_score * int(code[:-1].lstrip("0"))
    return total_score

with open('input.txt') as f:
    rows = f.read().strip().split("\n")

    # Part 1
    print(calculate_score(rows, (3 + 1)))

    # Part 2
    print(calculate_score(rows, (26 + 1)))
