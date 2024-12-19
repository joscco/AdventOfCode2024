from functools import cache

@cache
def number_of_matches(subdesign, patterns):
    if subdesign == "":
        return 1
    total = 0
    for pattern in patterns:
        if subdesign.startswith(pattern):
            total += number_of_matches(subdesign[len(pattern):], patterns)
    return total


with open('input.txt') as f:
    input = f.read().strip().split("\n\n")

    patterns = [brick for brick in input[0].split(", ")]
    designs = [pattern for pattern in input[1].split("\n")]

    # Part 1
    print(sum(number_of_matches(pattern, frozenset(patterns)) > 0 for pattern in designs))

    # Part 2
    print(sum(number_of_matches(pattern, frozenset(patterns)) for pattern in designs))
