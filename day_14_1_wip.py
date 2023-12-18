from functools import cache

def serialize(platform: list[str]) -> str:
    return "\n".join(platform)

def deserialize(platform: str) -> list[str]:
    return platform.split("\n")

def rotateAntiClockwise(platform: str) -> str:
    """Rotate matrix, turing north to west"""
    platform = deserialize(platform)
    width = len(platform)
    return serialize(["".join([platform[x][-y] for x in range(width)]) for y in range(1, width + 1)])

def rotate(platform: str) -> str:
    """Rotate matrix, turning north to east"""
    platform = deserialize(platform)
    width = len(platform)
    return serialize(["".join([platform[-x][y] for x in range(1, width + 1)]) for y in range(width)])

@cache
def spinCycle(platform: str) -> str:
    """Tilts and rotates platform four times"""
    newPlatform = platform
    for i in range(4):
        newPlatform = tiltPlatform(newPlatform)
        newPlatform = rotate(newPlatform)
    return newPlatform

def tiltPlatform(platform: str) -> str:
    """Slides all rocks to the beginning of their strings, i.e., left"""
    platform = deserialize(platform)
    platform = list(map(tiltRow, platform))
    return serialize(platform)

@cache
def tiltRow(row: str) -> str:
    """Slides rocks to the beginning of the string"""
    newRow = row
    for i, char in enumerate(row):
        if char == "O":
            newPos = findNewPos(newRow, i)
            newRow = newRow[:i] + "." + newRow[i+1:]
            newRow = newRow[:newPos] + "O" + newRow[newPos+1:]

    return newRow
        
def findNewPos(row: str, oldPos: int) -> int:
    """Find new position of one rock"""
    for i in range(oldPos - 1 , -1, -1):
        if row[i] != ".":
            return i + 1
    return 0

def countLoad(platform: str) -> int:
    """Count load on east support beam"""
    load = 0
    for i, row in deserialize(platform):
        for j, char in enumerate(row):
            if char == "O":
                score += len(row) - i
    return score

platform = open("input/day_14.txt").read()
# Rotate to start strings at north, turning north to east for the following
platform = rotateAntiClockwise(platform)

cycles = 1000000000
lastPlatform = platform
for i in range(cycles):
    print(f"Progress: {round(i/cycles * 100, 2)}%", end = "\r")
    platform = spinCycle(platform)
print(f"Load: {countLoad(platform)}")