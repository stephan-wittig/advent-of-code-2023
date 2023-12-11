from itertools import repeat
from typing import List

lines = open("input/day_11.txt").read().split("\n")

# Expand rows
for y in range(len(lines) - 1, -1, -1):
    if lines[y].find("#") < 0:
        lines.insert(y, "".join(repeat(".", len(lines[y]))))

# Expand columns
for x in range(len(lines[0]) -1, -1, -1):
    column = "".join(list(map(lambda r: r[x], lines)))
    if all(list(map(lambda s: s == ".", column))):
        for y in range(len(lines)):
            lines[y] = lines[y][:x] + "." + lines[y][x:]

class Galaxy:
    """Coordinates of a galaxy in the universe"""
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
def distanceBetween(g1: Galaxy, g2: Galaxy):
    return abs(g1.x - g2.x) + abs(g1.y - g2.y)
    
galaxies: List[Galaxy] = []
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append(Galaxy(x, y))

sumOfDistances = 0
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies[i+1:]):
        sumOfDistances += distanceBetween(g1, g2)

print(f"Sum of distances: {sumOfDistances}")