import re

with open("input.txt") as f:
    s = f.read()
    mul_matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    total_sum = sum(int(x) * int(y) for x, y in mul_matches)

    print(total_sum)

    # Part 2
    mul_matches = list(re.finditer(r"mul\((\d+),(\d+)\)", s))
    d_matches = sorted(re.finditer(r"do\(\)|don't\(\)", s), key=lambda x: x.start())
    total_sum = 0
    for mul_match in mul_matches:
        match_start = mul_match.start()

        last_action = None
        for d_match in d_matches:
            if d_match.start() < match_start:
                last_action = d_match
            else:
                break

        if last_action is None or last_action.group() == "do()":
            x, y = map(int, mul_match.groups())
            total_sum += x * y

    print(total_sum)




