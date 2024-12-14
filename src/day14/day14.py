import os
import re
from PIL import Image


def find_robot_position_after_moves(robots, times, width, height):
    positions = []
    for robot in robots:
        positions.append(((robot[0] + robot[2] * times) % width, (robot[1] + robot[3] * times) % height))
    return positions

def print_grid_as_image(after_positions, width, height):
    image = Image.new("1", (width, height), 1)  # 1 for white
    pixels = image.load()

    for position in after_positions:
        pixels[position[0], position[1]] = 0  # 0 for black

    # Create the directory if it doesn't exist
    os.makedirs("images", exist_ok=True)

    # Save the image
    image.save(f"images/i_{i}.png")


with open("input.txt") as f:
    data = f.read().strip().split("\n")

    pattern = re.compile(r"p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)")
    robots = []
    for block in data:
        matches = pattern.findall(block)
        if matches:
            robots.append([int(num) for match in matches for num in match])

    # Part 1
    width = 101
    height = 103
    after_positions = find_robot_position_after_moves(robots, 100, width, height)

    first, second, third, fourth = 0, 0, 0, 0
    for position in after_positions:
        if position[0] < width // 2 and position[1] < height // 2:
            first += 1
        if position[0] < width // 2 and position[1] > height // 2:
            second += 1
        if position[0] > width // 2 and position[1] < height // 2:
            third += 1
        if position[0] > width // 2 and position[1] > height // 2:
            fourth += 1

    print(first * second * third * fourth)

    # Part 2
    # Hoping that the christmas tree will be visible within the first 10000 iterations
    for i in range(10000):
        after_positions = find_robot_position_after_moves(robots, i, width, height)
        print_grid_as_image(after_positions, width, height)

