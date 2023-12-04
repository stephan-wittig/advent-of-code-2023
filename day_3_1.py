import regex as re

input = open('input/day_3.txt').read().split('\n')

allNumberMatches = []

for lineNumber, line in enumerate(input):
    for numberMatch in re.finditer("\d+", line):
        allNumberMatches.append({
            "line": lineNumber,
            "number": int(numberMatch.group(0)),
            "start": numberMatch.start(),
            "end": numberMatch.end()
        })

def getGearRatio(gearY: int, gearX: int):
    neighbourNumbers = list(filter(lambda n: 
                                   n["line"] <= gearY + 1 and n["line"] >= gearY - 1 and 
                                   #gearX + 1 <= n["end"] and gearX + 1 >= n["start"], 
                                   gearX <= n["end"] and gearX + 1  >= n["start"], 
                            allNumberMatches))
    if len(neighbourNumbers) != 2:
        return 0
    
    return neighbourNumbers[0]["number"] * neighbourNumbers[1]["number"]

sumOfGearRatios = 0

for gearY, line in enumerate(input):
    for gearMatch in re.finditer("\*", line):
        gearX = gearMatch.start()
        gearRatio = getGearRatio(gearY, gearX)
        sumOfGearRatios += gearRatio

print(sumOfGearRatios)

