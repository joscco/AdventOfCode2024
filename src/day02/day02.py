with open("input.txt") as f:
    s = [list(map(int, x.split(" "))) for x in f.read().split("\n")]

save_increase = lambda x, y: 1 <= y - x <= 3
save_decrease = lambda x, y: 1 <= x - y <= 3
save_increasing = lambda z: all(save_increase(z[j], z[j + 1]) for j in range(len(z) - 1))
save_decreasing = lambda z: all(save_decrease(z[j], z[j + 1]) for j in range(len(z) - 1))

all_decreasing_or_increasing_by_at_least_one = [
    save_increasing(x) or save_decreasing(x)
    for x in s]

print(sum(all_decreasing_or_increasing_by_at_least_one))

# Part 2
remove_index = lambda z, i: [z[j] for j in range(len(z)) if j != i]
save_increase_possible = lambda z: any(save_increasing(remove_index(z, i)) for i in range(len(z)))
save_decrease_possible = lambda z: any(save_decreasing(remove_index(z, i)) for i in range(len(z)))

all_decreasing_or_increasing_by_at_least_one = [
    save_increasing(x) or
    save_decreasing(x) or
    save_increase_possible(x) or
    save_decrease_possible(x)
    for x in s
]

print(sum(all_decreasing_or_increasing_by_at_least_one))


