import re

def hash(input: str) -> int:
    value = 0
    for c in input:
        value += ord(c)
        value = value * 17
        value = value % 256
    return value

class Lens:
    def __init__(self, label: str, focalLength: str) -> None:
        self.label = label
        self.focalLength = focalLength

    def __str__(self) -> str:
        return f"[{self.label} {self.focalLength}]"

class LensBox:
    def __init__(self) -> None:
        self.lenses: list[Lens] = []

    def remove(self, label: str) -> None:
        index, lens = self.getLens(label)
        if index >= 0:
            self.lenses.pop(index)

    def add(self, newLens: Lens) -> None:
        index, lens = self.getLens(newLens.label)
        if index < 0:
            self.lenses.append(newLens)
            return
        self.lenses[index] = newLens

    def getLens(self, label: str) -> (int, Lens):
        for i, l in enumerate(self.lenses):
            if l.label == label:
                return i, l
        return -1, None
    
    def countScore(self) -> int:
        return sum([(i + 1) * l.focalLength for i, l in enumerate(self.lenses)])
    
    def __str__(self) -> str:
        return " ".join([str(l) for l in self.lenses])

class LensLibrary:
    def __init__(self) -> None:
        self.boxes: dict[int, LensBox] = {i:LensBox() for i in range(0, 256)}

    def executeInstruction(self, instruction: str) -> None:
        eqMatch = re.match("(\w+)=(\d+)", instruction)
        if eqMatch:
            newLens = Lens(eqMatch.group(1), int(eqMatch.group(2)))
            boxNumber = hash(newLens.label)
            self.boxes[boxNumber].add(newLens)
            return
        
        label = instruction[:-1]
        boxNumber = hash(label)
        self.boxes[boxNumber].remove(label)

    def countScore(self) -> int:
        return sum([(i + 1) * lb.countScore() for i, lb in self.boxes.items()])

    def __str__(self) -> str:
        return "\n".join([f"Box {i}: {b}" for i, b in self.boxes.items()])

instructions = open("input/day_15.txt").read().split(",")

lib = LensLibrary()
for ins in instructions:
    lib.executeInstruction(ins)

print(lib.countScore())