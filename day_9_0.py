from typing import List
from multiprocessing import Pool

def parseLine(line: str) -> List[int]:
    return list(map(int, line.split(" ")))
    
def derive(values: List[int]) -> List[List[int]]:
    output = [ values ]
    while (not output[-1]) or any(output[-1]):
        nextDerivation = []
        for i in range(len(output[-1]) - 1):
            nextDerivation.append(output[-1][i +1] - output[-1][i])
        output.append(nextDerivation)
    return output[0:-1]

def interpolate(derivations: List[List[int]]) -> int:
    lastInterpolation = 0
    for i in range(len(derivations) - 1, -1, -1):
        lastInterpolation += derivations[i][-1]
    return lastInterpolation


if __name__ == '__main__':
    input = open('input/day_9.txt').read().split("\n")
    with Pool(8) as p:
        lines = p.map(parseLine, input)
        allDerivations = p.map(derive, lines)
        nextValues = p.map(interpolate, allDerivations)
        print(nextValues)
    print(f"Result: {sum(nextValues)}")