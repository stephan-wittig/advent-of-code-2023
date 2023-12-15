rows = open("input/day_14.txt").read().split("\n")
columns = ["".join(t) for t in zip(*rows)]

def tiltColumn(col: str) -> str:
    newCol = col
    for i, char in enumerate(col):
        if char == "O":
            newPos = findNewPos(newCol, i)
            newCol = newCol[:i] + "." + newCol[i+1:]
            newCol = newCol[:newPos] + "O" + newCol[newPos+1:]

    return newCol
        

def findNewPos(col: str, oldPos: int) -> int:
    for i in range(oldPos - 1 , -1, -1):
        if col[i] != ".":
            return i + 1
    return 0

def countScore(col: str) -> int:
    score = 0
    for i, c in enumerate(col):
        if c == "O":
            score += len(col) - i
    return score

score = sum([countScore(tiltColumn(col)) for col in columns])
print(score)