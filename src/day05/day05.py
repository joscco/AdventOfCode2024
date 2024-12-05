with open("input.txt") as f:
    s = f.read().split("\n\n")
    rules = [list(map(int, x.split("|"))) for x in s[0].split("\n")]
    orders = [list(map(int, x.split(","))) for x in s[1].split("\n")]

    def is_correct_order(order, later_than):
        return all(order[i] not in later_than or order[j] not in later_than[order[i]] for i in range(1, len(order)) for j in range(i))

    later_than = {}
    for first, second in rules:
        later_than.setdefault(first, []).append(second)

    right_orders = [order for order in orders if is_correct_order(order, later_than)]
    print(sum(order[len(order) // 2] for order in right_orders))

    # Part 2
    def reorder_order(order, later_than):
        ordered = []
        while order:
            for i, potential_next in enumerate(order):
                if potential_next not in later_than or all(successor not in order for successor in later_than[potential_next]):
                    ordered.append(order.pop(i))
                    break
        return ordered

    false_orders = [order for order in orders if not is_correct_order(order, later_than)]
    reordered_orders = [reorder_order(order, later_than) for order in false_orders]
    print(sum(order[len(order) // 2] for order in reordered_orders))