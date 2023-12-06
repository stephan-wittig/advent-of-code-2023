import re
from operator import mul
from functools import reduce

lines = open('input/day_6.txt').read().split('\n')

def parseList(input: str):
    return list(map(lambda s: int(s), re.split("\s+", input)[1:]))

parsedLists = list(map(parseList, lines))

races = (zip(parsedLists[0], parsedLists[1]))

def checkWin(race: tuple[int, int], speed: int):
    runtime = race[0] - speed
    return speed * runtime > race[1]

def countWinOptions(race: tuple[int, int]):
    return list(map(lambda speed: checkWin(race, speed), range(1, race[0]))).count(True)


numbersOfWinOptions = list(map(countWinOptions, races))

print(numbersOfWinOptions)

result = reduce(lambda x, y: x * y, numbersOfWinOptions)
print(f"Result: {result}")