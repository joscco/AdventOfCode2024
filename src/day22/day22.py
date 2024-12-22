with open('input.txt') as f:
    rows = f.read().strip().split("\n")

    def next_secret(num):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        return num

    def next_n_secrets(num, n):
        result = [num]
        for _ in range(n):
            result.append(next_secret(result[-1]))
        return result

    secret_sequences = [next_n_secrets(int(n), 2000) for n in rows]

    print(sum(map(lambda l: l[-1], secret_sequences)))

    ## Part 2
    def delta_to_bananas_map(secret_sequence):
        last_digits = list(map(lambda x: x % 10, secret_sequence))
        bananas_for_deltas = {}
        for i in range(4, 2001):
            price_deltas = (last_digits[i - 3] - last_digits[i - 4], last_digits[i - 2] - last_digits[i - 3], last_digits[i - 1] - last_digits[i - 2], last_digits[i] - last_digits[i - 1])
            if price_deltas not in bananas_for_deltas:
                bananas_for_deltas[price_deltas] = last_digits[i]

        return bananas_for_deltas

    total_delta_to_bananas_map = {}
    for secret_sequence in secret_sequences:
        for key, val in delta_to_bananas_map(secret_sequence).items():
            total_delta_to_bananas_map[key] = total_delta_to_bananas_map.get(key, 0) + val

    print(max(total_delta_to_bananas_map.values()))
