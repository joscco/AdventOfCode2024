with open("input.txt") as f:
    values = [list(line) for line in f.read().split("\n")]


    def get_neighborIndices(i, j):
        return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


    def find_component(i, j, visited_positions) -> set:
        component = set()
        stack = [(i, j)]
        value = values[j][i]
        while stack:
            current = stack.pop()
            if current in component or current in visited_positions:
                continue
            visited_positions.add(current)
            component.add(current)
            for neighbor in get_neighbors_of_same_value(*current, value):
                stack.append(neighbor)
        return component

    def get_neighbors_of_same_value(i, j, value) -> list:
        result = []
        for neighborIndex in get_neighborIndices(i, j):
            if 0 <= neighborIndex[1] < len(values) and 0 <= neighborIndex[0] < len(values[0]) and \
                    values[neighborIndex[1]][neighborIndex[0]] == value:
                result.append(neighborIndex)
        return result


    def get_connected_components(grid):
        components = []
        visited_positions = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited_positions:
                    continue
                components.append(find_component(i, j, visited_positions))
        return components


    def get_perimeter_length(component):
        perimeter = 0
        for position in component:
            stone_perimeter = 4
            for neighborIndex in get_neighborIndices(*position):
                if neighborIndex in component:
                    stone_perimeter -= 1
            perimeter += stone_perimeter
        return perimeter


    def get_area(component):
        return len(component)


    def get_product(component):
        return get_area(component) * get_perimeter_length(component)

    print(sum([get_product(component) for component in get_connected_components(values)]))

    # Part 2

    def get_number_of_sides(component):
        sides = []
        seen = set(component)
        for n in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for edge in sorted({(s[0] + n[0], s[1] + n[1]) for s in seen} - seen, key=lambda p: (p[0], p[1])):
                exists = next((side for side in sides for p, d in side if
                               abs(p[0] - edge[0]) + abs(p[1] - edge[1]) == 1 and d == n), None)
                exists.add((edge, n)) if exists else sides.append({(edge, n)})
        return len(sides)


    def get_product_2(component):
        return get_area(component) * get_number_of_sides(component)


    print(sum([get_product_2(component) for component in get_connected_components(values)]))
