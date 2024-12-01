with open("input.txt") as f:
    s = [list(map(int, x.split("   "))) for x in f.read().split("\n")]

left, right = zip(*s)
left, right = sorted(left), sorted(right)

print(sum(abs(x - y) for x, y in zip(left, right)))
print(sum(x * right.count(x) for x in left))