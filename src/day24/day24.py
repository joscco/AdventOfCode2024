with open("input.txt") as f:
    wires = {}
    operations = []

    def process(operator, a, b):
        if operator == "AND":
            return a & b
        elif operator == "OR":
            return a | b
        elif operator == "XOR":
            return a ^ b

    highest_z = "z00"
    input, wire_data = f.read().split("\n\n")

    for line in input.split("\n"):
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
    for line in wire_data.split("\n"):
        a, op, b, _, result = line.split(" ")
        operations.append((a, op, b, result))
        if result[0] == "z" and int(result[1:]) > int(highest_z[1:]):
            highest_z = result

    fishy_results = set()
    for a, op, b, result in operations:
        # For a binary adder, all resulting z's must be like z_n = (A XOR B) XOR C_in
        # All COuts must be like C_out = A AND B OR (C_in AND (A XOR B))

        # For final z (highest z), there must be a final XOR operation
        if result[0] == "z" and op != "XOR" and result != highest_z:
            fishy_results.add(result)

        # For all XORs, check that either xs and ys are involved (A XOR B) or the result is a z
        if (
                op == "XOR"
                and result[0] != "z"
                and a[0] not in ["x", "y"]
                and b[0] not in ["x", "y"]
        ):
            fishy_results.add(result)

        # For all ANDs (except the first for x00), check that an OR is the previous operation
        if op == "AND" and "x00" not in [a, b]:
            for sub_a, sub_op, sub_b, sub_result in operations:
                if (result == sub_a or result == sub_b) and sub_op != "OR":
                    fishy_results.add(result)

    while len(operations):
        a, op, b, result = operations.pop(0)
        if a in wires and b in wires:
            wires[result] = process(op, wires[a], wires[b])
        else:
            operations.append((a, op, b, result))

    bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
    print(int("".join(bits), 2))

    # Part 2
    print(",".join(sorted(fishy_results)))