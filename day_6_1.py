import re
from functools import reduce
from multiprocessing import Pool

input = open('input/day_6.txt').read()

parsedSValues = re.match("Time:\s+([\d ]+)\nDistance:\s+([\d ]+)", input).groups()
parsedNValues = list(map(lambda s: int(s.replace(" ", "")), parsedSValues))
time = parsedNValues[0]
dist = parsedNValues[1]

def checkWin(speed: int):
    runtime = time - speed
    return speed * runtime > dist

if __name__ == '__main__':
    with Pool(8) as p:
        raceResults = p.map(checkWin, range(1, time))
    result = raceResults.count(True)
    print(f"Result: {result}")