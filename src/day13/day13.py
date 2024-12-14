import re

with open("input.txt") as f:
    data = f.read().strip().split("\n\n")

    pattern = re.compile(r"X\s*[+=]\s*(\d+),\s*Y\s*[+=]\s*(\d+)")
    sets = []

    for block in data:
        matches = pattern.findall(block)
        if matches:
            sets.append([int(num) for match in matches for num in match])


    def invert_matrix(a):
        norm = 1.0 / ((a[0][0] * a[1][1]) - (a[0][1] * a[1][0]))
        a_inv = [[a[1][1] * norm, -a[0][1] * norm], [-a[1][0] * norm, a[0][0] * norm]]
        return a_inv


    def mult(a, b):
        return [a[0][0] * b[0] + a[0][1] * b[1], a[1][0] * b[0] + a[1][1] * b[1]]


    def nearest_int(x, max_diff=1e-3):
        x0 = int(x)
        if x - x0 < max_diff:
            return x0
        if x - x0 > 1 - max_diff:
            return x0 + 1
        return -1


    def find_minimal_tokens(set, offset=0):
        a_inv = invert_matrix([[set[0], set[2]], [set[1], set[3]]])
        n = mult(a_inv, [set[4] + offset, set[5] + offset])
        na = nearest_int(n[0])
        nb = nearest_int(n[1])
        if na >= 0 and nb >= 0:
            return 3 * na + nb
        return 0


    print(sum(find_minimal_tokens(set) for set in sets))

    # Part 2

    print(sum(find_minimal_tokens(set, 10000000000000) for set in sets))
