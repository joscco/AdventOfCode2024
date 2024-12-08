def vector_add(v1, v2):
    return v1[0] + v2[0], v1[1] + v2[1]

def vector_sub(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1]

def is_in_grid(v):
    return 0 <= v[0] < width and 0 <= v[1] < height

with open("input.txt") as f:
    lines = [list(line) for line in f.read().split("\n")]
    height, width = len(lines), len(lines[0])

letter_map = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != ".":
            letter_map.setdefault(char, []).append((j, i))


def calculate_unique_positions(part2=False):
    unique_new_pos = set()
    for letter_line in letter_map.values():
        for i in range(len(letter_line)):
            for j in range(i + 1, len(letter_line)):
                first_pos, second_pos = letter_line[i], letter_line[j]
                difference = vector_sub(second_pos, first_pos)
                if part2:
                    unique_new_pos.update([first_pos, second_pos])
                    first_ext = vector_add(second_pos, difference)
                    while is_in_grid(first_ext):
                        unique_new_pos.add(first_ext)
                        first_ext = vector_add(first_ext, difference)
                    second_ext = vector_sub(first_pos, difference)
                    while is_in_grid(second_ext):
                        unique_new_pos.add(second_ext)
                        second_ext = vector_sub(second_ext, difference)
                else:
                    first_ext = vector_add(second_pos, difference)
                    if is_in_grid(first_ext):
                        unique_new_pos.add(first_ext)
                    second_ext = vector_sub(first_pos, difference)
                    if is_in_grid(second_ext):
                        unique_new_pos.add(second_ext)
    return unique_new_pos


unique_positions = calculate_unique_positions()
print(len(unique_positions))

# Part 2
unique_positions_extended = calculate_unique_positions(True)
print(len(unique_positions_extended))
