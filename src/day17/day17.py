with open('input.txt') as f:
    data = f.read().strip().split("\n")

    A = int(data[0].replace("Register A: ", ""))
    B = int(data[1].replace("Register B: ", ""))
    C = int(data[2].replace("Register C: ", ""))

    program = [int(x) for x in data[4].replace("Program: ", "").split(",")]


    def run(a, b, c, program, part2=False):
        reg_a = a
        reg_b = b
        reg_c = c
        out = []
        i = 0
        while i < len(program):
            opcode = program[i]
            literal_operand = program[i + 1]
            i += 2

            combo_operand = literal_operand
            match combo_operand:
                case 4:
                    combo_operand = reg_a
                case 5:
                    combo_operand = reg_b
                case 6:
                    combo_operand = reg_c

            match opcode:
                case 0:
                    reg_a = reg_a >> combo_operand
                case 1:
                    reg_b = reg_b ^ literal_operand
                case 2:
                    reg_b = combo_operand % 8
                case 3:
                    i = literal_operand if reg_a != 0 else i
                case 4:
                    reg_b = reg_b ^ reg_c
                case 5:
                    out.append(combo_operand % 8)
                case 6:
                    reg_b = reg_a >> combo_operand
                case 7:
                    reg_c = reg_a >> combo_operand
        return out


    output = run(A, B, C, program)
    output = ",".join(map(str, output))
    print(f"Part 1: {output}")

    # Part 2
    print("Part 2")
    cofactors = [[]]
    a_value = 0
    best = 0
    solutions = []

    # Use recursive solving
    for i in range(len(program)):
        print()
        found = False
        for j in range(0, 9):
            for c in [l for l in cofactors if len(l) == i]:
                A = sum([k * 8 ** (len(c) - n) for n, k in enumerate(c)]) + j
                output = run(A, B, C, program)
                # print("A", A)
                # print("Output", output)
                if program == output:
                    solutions.append(A)
                if program[-(i+1):] == output:
                    cofactors.append([*c, j])
                    print(c, sum([k * 8 ** (len(c) - n) for n, k in enumerate(c)]), output)
                    found = True
        if not found:
            print("No match")
    print(min(solutions))

