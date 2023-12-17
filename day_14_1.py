from functools import cache

def transpose(platform: list[str]) -> list[str]:
    """Transpose the matrix, swapping north to east"""
    return ["".join(t) for t in zip(*platform)]

def rotateAntiClockwise(platform: list[str]) -> list[str]:
    """Rotate matrix, turing north to west"""
    width = len(platform)
    return ["".join([platform[x][-y] for x in range(width)]) for y in range(1, width + 1)]

def rotate(platform: list[str]) -> list[str]:
    """Rotate matrix, turning north to east"""
    width = len(platform)
    return ["".join([platform[-x][y] for x in range(1, width + 1)]) for y in range(width)]

def spinCycle(platform: list[str]) -> list[str]:
    """Tilts and rotates platform four times"""
    newPlatform = platform
    for i in range(4):
        newPlatform = tiltPlatform(newPlatform)
        newPlatform = rotate(newPlatform)
    return newPlatform

def tiltPlatform(platform: list[str]) -> list[str]:
    """Slides all rocks to the beginning of their strings, i.e., left"""
    return [tiltRow(col) for col in platform]

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

def countLoad(platform: list[str]) -> int:
    """Count load on east support beam"""
    load = 0
    for i, row in platform:
        for j, char in enumerate(row):
            if char == "O":
                score += len(row) - i
    return score

platform = open("input/day_14.txt").read().split("\n")
# Rotate to start strings at north, turning north to east for the following
platform = rotateAntiClockwise(platform)

cycles = 1000000000
for i in range(cycles):
    print(f"Progress: {i/cycles * 100}%")
    platform = spinCycle(platform)
    #print("\n".join(rotate(platform)) + "\n")
print(f"Load: {countLoad(platform)}")