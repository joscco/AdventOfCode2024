with open("input.txt") as f:
    data = f.read()

def checksum(line):
    return sum(i * int(char) for i, char in enumerate(line) if char != ".")

long_line, free_spaces, files = [], [], []
for i, char in enumerate(data):
    if not i % 2:
        files.append((str(i // 2), len(long_line), int(char)))
        long_line.extend([str(i // 2)] * int(char))
    else:
        free_spaces.append((len(long_line), int(char)))
        long_line.extend("." * int(char))

def part_1():
    res, i, j = [], 0, len(long_line) - 1
    while j > i:
        if long_line[i] == ".":
            res.append(long_line[j])
            j -= 1
            while long_line[j] == ".":
                j -= 1
        else:
            res.append(long_line[i])
        i += 1
    if long_line[i] != ".":
        res.append(long_line[i])
    return res

print(checksum(part_1()))

def part_2():
    while files:
        file_id, file_idx, file_count = files.pop()
        for index, (free_idx, free_count) in enumerate(free_spaces):
            if free_idx > file_idx:
                break
            if free_count >= file_count:
                long_line[free_idx:free_idx + file_count] = [file_id] * file_count
                long_line[file_idx:file_idx + file_count] = ["."] * file_count
                free_spaces[index] = (free_idx + file_count, free_count - file_count)
                break
    return long_line

print(checksum(part_2()))