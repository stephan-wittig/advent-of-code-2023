from itertools import repeat
from typing import List

lines = open("input/day_11.txt").read().split("\n")

expandedWeight = 10**6
columnWeights = list(repeat(1, len(lines[0])))
rowWeights =  list(repeat(1, len(lines)))

# Expand rows
for y in range(len(lines) - 1, -1, -1):
    if lines[y].find("#") < 0:
        rowWeights[y] = expandedWeight

# Expand columns
for x in range(len(lines[0]) -1, -1, -1):
    column = "".join(list(map(lambda r: r[x], lines)))
    if column.find("#") < 0:
        columnWeights[x] = expandedWeight

class Galaxy:
    """Coordinates of a galaxy in the universe"""
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
def distanceBetween(g1: Galaxy, g2: Galaxy):
    x = sorted([g1.x, g2.x])
    y = sorted([g1.y, g2.y])
    weightedDistance = 0

    weightedDistance += sum(columnWeights[x[0]:x[1]])
    weightedDistance += sum(rowWeights[y[0]:y[1]])

    return weightedDistance
    
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