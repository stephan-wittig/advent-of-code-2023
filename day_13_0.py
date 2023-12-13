

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

        if "\n".join(left) == "\n".join(reversed(right)):
            return i
    return 0

totalScore = sum([getScore(b) for b in blocks])
print(f"Result: {totalScore}")