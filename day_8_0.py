import re
from itertools import cycle

input = open('input/day_8.txt').read()
start = "AAA"
target = "ZZZ"

instructionsMatch = re.search("^[LR]+$", input, flags=re.MULTILINE)
if instructionsMatch == None:
    raise ValueError("Cannot parse instructions")
instructions = instructionsMatch.group(0)

nodes = {}

for nodesMatch in re.finditer("^(\w+) = \((\w+), (\w+)\)$", input, flags=re.MULTILINE):
    nodes[nodesMatch.group(1)] = {"L": nodesMatch.group(2), "R": nodesMatch.group(3)}

pos = start

for i, instruction in enumerate(cycle(instructions)):
    print(f"Pos: {pos}, Ins: {instruction}")
    if pos == target:
        print(f"Arrived after {i}")
        break
    pos = nodes[pos][instruction]
