with open("input.txt") as f:
    stones = f.read().split(" ")
    stone_rules = {}
    initial_stones = {stone: stones.count(stone) for stone in set(stones)}

    def find_next(x) -> list:
        if x == "0":
            return ["1"]
        if len(x) % 2 == 0:
            half = len(x) // 2
            return [str(int(x[:half])), str(int(x[half:]))]
        return [str(int(x) * 2024)]

    def generate_stones(n, start_stones):
        cur_stones = start_stones
        for _ in range(n):
            new_stones = {}
            for x, count in cur_stones.items():
                for y in stone_rules.get(x, find_next(x)):
                    new_stones[y] = new_stones.get(y, 0) + count
            cur_stones = new_stones
        return cur_stones

    print(sum(generate_stones(25, initial_stones).values()))

    # Part 2
    print(sum(generate_stones(75, initial_stones).values()))
