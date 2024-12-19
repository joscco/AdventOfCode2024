from heapq import heappop, heappush
from math import inf

with open('input.txt') as f:
    maze = [list(l.strip()) for l in f]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i, l in enumerate(maze):
        for j, c in enumerate(l):
            if c == "S":
                start = (i, j)
            elif c == "E":
                end = (i, j)

    visited = dict()
    queue = list()
    highscore = inf
    paths = list()

    heappush(queue, (0, start, (1, 0), ""))
    while queue:
        score, pos, direction, path = heappop(queue)
        if score > highscore:
            break
        if (pos, direction) in visited and visited[(pos, direction)] < score:
            continue
        visited[(pos, direction)] = score
        if pos == end:
            highscore = score
            paths.append(path)
        forward_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if maze[forward_pos[1]][forward_pos[0]] != "#":
            heappush(queue, (score + 1, forward_pos, direction, path + "F"))
        heappush(queue, (score + 1000, pos, (-direction[1], direction[0]), path + "R"))
        heappush(queue, (score + 1000, pos, (direction[1], -direction[0]), path + "L"))

    tiles = set()
    tiles.add(start)
    for fullPath in paths:
        t, direction = (start, (1, 0))
        for node in fullPath:
            if node == "L":
                direction = (direction[1], -direction[0])
            elif node == "R":
                direction = (-direction[1], direction[0])
            elif node == "F":
                t = (t[0] + direction[0], t[1] + direction[1])
                tiles.add(t)
    print(f"Shortest path: {highscore}")
    print(f"Optimal viewing positions: {len(tiles)}")
