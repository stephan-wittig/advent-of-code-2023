import re
from itertools import cycle
from math import lcm


input = open('input/day_8.txt').read()

instructionsMatch = re.search("^[LR]+$", input, flags=re.MULTILINE)
if instructionsMatch == None:
    raise ValueError("Cannot parse instructions")
instructions = instructionsMatch.group(0)

nodes = {}

for nodesMatch in re.finditer("^(\w+) = \((\w+), (\w+)\)$", input, flags=re.MULTILINE):
    nodes[nodesMatch.group(1)] = {"L": nodesMatch.group(2), "R": nodesMatch.group(3)}

class Path:
    def __init__(self, pos: str) -> None:
        self.startPos = pos
        self.pos = pos

    def move(self, instruction: str) -> str:
        self.pos = nodes[self.pos][instruction]
        return self.pos
    
    def reset(self):
        self.pos = self.startPos

    def isFinished(self) -> bool:
            return self.pos[-1] == "Z"
    
    def solve(self) -> int:
        for i, ins in enumerate(cycle(instructions), 1):
            self.move(ins)
            if self.isFinished():
                return i

    def __str__(self) -> str:
        return f"{self.pos}"

startNodes = list(filter(lambda n: n[-1] == "A", nodes.keys()))
paths = list(map(lambda n: Path(n), startNodes))

solutions = list(map(lambda p: p.solve(), paths))
print(solutions)
result = lcm(*solutions)

print(f"Result: {result}")
