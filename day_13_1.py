

input = open("input/day_13.txt").read()

blocks = input.split("\n\n")

def getScore(block: str) -> int:
    rows = block.split("\n")
    columns = ["".join(t) for t in zip(*rows)]

    return findAxis(rows) * 100 + findAxis(columns)

def findAxis(block: list[str]) -> int:
    for i in range(1, len(block)):
        width = min(i, len(block) - i)
        left = block[i-width:i]
        right = block[i:i+width]

        print(f"{left}\n\n{right}")

        if compareWithSmudge(left, right):
            return i
    return 0

def compareWithSmudge(left: list[str], right: list[str]) -> bool:
    left = "\n".join(left)
    length = len(left)
    left = iter(left)
    right = iter("\n".join(reversed(right)))

    smudgeFound = False
    for i in range(length):
        if next(left) == next(right):
            continue
        if smudgeFound:
            return False
        print(f"Smudge found at {i}")
        smudgeFound = True
    return smudgeFound

totalScore = sum([getScore(b) for b in blocks])
print(f"Result: {totalScore}")