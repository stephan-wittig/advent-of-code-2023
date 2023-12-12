from typing import List, Iterable, Tuple
from itertools import combinations
import re

rows = open("input/day_12.txt").read().split("\n")

def findUnknowns(pattern: str) -> List[int]:
    unknowns = []
    for i, char in enumerate(pattern):
        if char == "?":
            unknowns.append(i)
    
    return unknowns

class Row:
    def __init__(self, s: str) -> None:
        [self.pattern, groups] = s.split(" ")
        self.groups = list(map(int, groups.split(",")))
        self.unknownIndexes = findUnknowns(self.pattern)

    def __str__(self) -> str:
        return f"{self.pattern} {self.groups} {self.unknownIndexes}"
    
    def combinations(self) -> Iterable[Tuple[int]]:
        missing = sum(self.groups) - self.pattern.count("#")
        return combinations(self.unknownIndexes, missing)
    
    def replacePattern(self, combination: Tuple[int]) -> str:
        newString = ""
        for i, c in enumerate(self.pattern):
            if c != "?":
                newString += c
                continue
            if i in combination:
                newString += "#"
                continue
            newString += "."
        return newString
    
    def testString(self, s: str) -> bool:
        matches = re.findall("#+", s)

        if len(matches) != len(self.groups):
            return False

        for i, m in enumerate(matches):
            if len(m) != self.groups[i]:
                return False

        return True
    
def getValidArrangements(r: Row) -> int:
    result = 0
    for c in r.combinations():
        s = r.replacePattern(c)
        isValid = r.testString(s)
        result += isValid
    return result

result = 0
for row in map(Row, rows):
    result += getValidArrangements(row)

print(f"Result: {result}")
