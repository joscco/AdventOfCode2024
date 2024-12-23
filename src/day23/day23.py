with open('input.txt') as f:
    rows = [line.split("-") for line in f.read().strip().split("\n")]

    connections = {}
    for row in rows:
        connections.setdefault(row[0], []).append(row[1])
        connections.setdefault(row[1], []).append(row[0])

    # Part 1:
    connected_triplets = set()
    for base_node, values in connections.items():
        if len(values) >= 2:
            for i in range(len(values)):
                for j in range(i + 1, len(values)):
                    if values[i] in connections[values[j]]:
                        if base_node.startswith("t") or values[i].startswith("t") or values[j].startswith("t"):
                            connected_triplets.add(frozenset([base_node, values[i], values[j]]))

    print(len(connected_triplets))

    # Part 2
    largest_component = frozenset()
    for base_node in connections:
        component = set()
        todo = [base_node]
        while todo:
            current = todo.pop()
            if current in component:
                continue
            if any(current not in connections[other] for other in component):
                continue
            component.add(current)
            todo.extend(connections[current])
        if len(component) > len(largest_component):
            largest_component = component

    print(",".join(sorted(list(largest_component))))
