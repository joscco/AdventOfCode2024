with open('input.txt') as f:
    data = f.read().strip().split("\n\n")

    movement_orders = [(1, 0) if char == '>' else (0, 1) if char == 'v' else (-1, 0) if char == '<' else (0, -1) for char in data[1].replace("\n", "")]

    grid_data = data[0].strip().split("\n")
    grid = [list(line) for line in grid_data]

    walls = {(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '#'}
    stones = {(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == 'O'}
    start = next((x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == '@')

    def try_to_move(stone, direction):
        old_stones_to_move, new_stones_to_add = set(), set()
        new_stone_position = (stone[0] + direction[0], stone[1] + direction[1])
        if new_stone_position in walls:
            return None
        if new_stone_position in stones:
            result = try_to_move(new_stone_position, direction)
            if not result:
                return None
            old_stones_to_move.update(result[0])
            new_stones_to_add.update(result[1])
        old_stones_to_move.add(stone)
        new_stones_to_add.add(new_stone_position)
        return old_stones_to_move, new_stones_to_add

    position = start
    for order in movement_orders:
        new_position = (position[0] + order[0], position[1] + order[1])
        if new_position in walls:
            continue
        if new_position in stones:
            result = try_to_move(new_position, order)
            if not result:
                continue
            old_stones_to_move, new_stones_to_add = result
            stones -= old_stones_to_move
            stones.update(new_stones_to_add)
        position = new_position

    print(sum(stone[0] + stone[1] * 100 for stone in stones))

    adapted_grid_data = data[0].replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")
    other_grid = [list(line) for line in adapted_grid_data.strip().split("\n")]

    walls = {(x, y) for y, line in enumerate(other_grid) for x, char in enumerate(line) if char == '#'}
    stones = {((x, y), (x+1, y)) for y, line in enumerate(other_grid) for x, char in enumerate(line) if char == '['}
    start = next((x, y) for y, line in enumerate(other_grid) for x, char in enumerate(line) if char == '@')

    def try_to_move_2(stone, direction):
        old_stones_to_move, new_stones_to_add = set(), set()
        new_stone_positions = ((stone[0][0] + direction[0], stone[0][1] + direction[1]), (stone[1][0] + direction[0], stone[1][1] + direction[1]))
        if any(pos in walls for pos in new_stone_positions):
            return None
        for new_stone_position in new_stone_positions:
            if any(new_stone_position in o_stone for o_stone in stones if o_stone != stone):
                new_stone = next(o_stone for o_stone in stones if new_stone_position in o_stone)
                result = try_to_move_2(new_stone, direction)
                if not result:
                    return None
                old_stones_to_move.update(result[0])
                new_stones_to_add.update(result[1])
        old_stones_to_move.add(stone)
        new_stones_to_add.add(new_stone_positions)
        return old_stones_to_move, new_stones_to_add

    position = start
    for order in movement_orders:
        new_position = (position[0] + order[0], position[1] + order[1])
        if new_position in walls:
            continue
        if any(new_position in stone for stone in stones):
            current_stone = next(stone for stone in stones if new_position in stone)
            result = try_to_move_2(current_stone, order)
            if not result:
                continue
            old_stones_to_move, new_stones_to_add = result
            stones -= old_stones_to_move
            stones.update(new_stones_to_add)
        position = new_position

    print(sum(stone[0][0] + stone[0][1] * 100 for stone in stones))