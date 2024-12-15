def draw_grid(grid, walls, stones, position):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in stones:
                print("O", end="")
            elif (x, y) == position:
                print("@", end="")
            else:
                print(".", end="")
        print()


def draw_grid_2(gr, walls, stones, position):
    for y, line in enumerate(gr):
        for x, char in enumerate(line):
            if (x, y) in walls:
                print("#", end="")
            elif tuple([(x, y), (x+1, y)]) in stones:
                print("[", end="")
            elif tuple([(x-1, y), (x, y)]) in stones:
                print("]", end="")
            elif (x, y) == position:
                print("@", end="")
            else:
                print(".", end="")
        print()


with open("input.txt") as f:
    data = f.read().strip().split("\n\n")

    # Read the movement orders
    movement_data = data[1].replace("\n", "")
    movement_orders = []
    for char in movement_data:
        if char == '>':
            movement_orders.append((1, 0))
        elif char == 'v':
            movement_orders.append((0, 1))
        elif char == '<':
            movement_orders.append((-1, 0))
        elif char == '^':
            movement_orders.append((0, -1))

    # Part 1
    # Read the grid
    grid_data = data[0].strip().split("\n")
    grid = [list(line) for line in grid_data]

    walls = set()
    stones = set()
    start = None

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            if char == 'O':
                stones.add((x, y))
            if char == '@':
                start = (x, y)

    # Part 1, Operators
    position = start
    for order in movement_orders:
        new_position = (position[0] + order[0], position[1] + order[1])
        if new_position in walls:
            continue
        if new_position in stones:
            old_stones_to_move = set()
            new_stones_to_add = set()
            current_stone = new_position
            while current_stone in stones:
                new_stone_position = (current_stone[0] + order[0], current_stone[1] + order[1])
                old_stones_to_move.add(current_stone)
                new_stones_to_add.add(new_stone_position)
                current_stone = new_stone_position
            # We cannot move
            if current_stone in walls:
                continue
            stones = stones - old_stones_to_move
            stones.update(new_stones_to_add)
        position = new_position

    draw_grid(grid, walls, stones, position)

    print(sum([(stone[0] + stone[1] * 100) for stone in stones]))

    # Part 2
    adapted_grid_data = data[0].replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")

    new_grid_data = adapted_grid_data.strip().split("\n")
    other_grid = [list(line) for line in new_grid_data]

    walls = set()
    stones = set()
    start = None

    for y, line in enumerate(other_grid):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            if char == '[':
                stones.add(tuple([(x, y), (x+1, y)]))
            if char == '@':
                start = (x, y)

    # Part 2, Operators
    def try_to_move(stone, direction):
        old_stones_to_move = set()
        new_stones_to_add = set()
        new_stone_positions = tuple([(stone[0][0] + direction[0], stone[0][1] + direction[1]), (stone[1][0] + direction[0], stone[1][1] + direction[1])])
        if any([position in walls for position in new_stone_positions]):
            return False
        # Check if there are other stones at any of new_stone_positions. Try to move them if so
        for new_stone_position in new_stone_positions:
            if any([new_stone_position in o_stone for o_stone in stones if o_stone != stone]):
                # Find stone at new position
                new_stone = None
                for other_stone in stones:
                    if new_stone_position in other_stone:
                        new_stone = other_stone
                        break
                result = try_to_move(new_stone, direction)
                if not result:
                    return False
                old_stones_to_move.update(result[0])
                new_stones_to_add.update(result[1])

        old_stones_to_move.add(stone)
        new_stones_to_add.add(new_stone_positions)
        return old_stones_to_move, new_stones_to_add

    draw_grid_2(other_grid, walls, stones, start)
    position = start
    for order in movement_orders:
        new_position = (position[0] + order[0], position[1] + order[1])
        if new_position in walls:
            continue
        if any([new_position in stone for stone in stones]):
            # Find stone at new position
            current_stone = None
            for stone in stones:
                if new_position in stone:
                    current_stone = stone
                    break

            result = try_to_move(current_stone, order)
            if not result:
                # No move was possible
                continue
            old_stones_to_move, new_stones_to_add = result
            stones = stones - old_stones_to_move
            stones.update(new_stones_to_add)
        position = new_position

    draw_grid_2(other_grid, walls, stones, position)

    print(sum([(stone[0][0] + stone[0][1] * 100) for stone in stones]))
