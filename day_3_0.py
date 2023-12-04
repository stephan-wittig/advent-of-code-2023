import regex as re

input = open('input/day_3.txt').read().split('\n')

def checkIfPartNumber(line: int, start: int, end: int):
    neighbours = ""

    for lineIndex in range(line - 1, line + 2):
        if lineIndex >= 0 and lineIndex < len(input):
            lineStr = input[lineIndex]
            neighbours += lineStr[max(start - 1, 0):min(end + 1, len(lineStr))]
    
    result = re.search("[^\d\.]", neighbours) != None
    return result

sumOfPartNumbers = 0

for lineIndex, line in enumerate(input):
    for numberMatch in re.finditer("\d+", line):
        partNumber = int(numberMatch.group(0))
        startIndex = numberMatch.start()
        endIndex = numberMatch.end()
        if checkIfPartNumber(lineIndex, startIndex, endIndex):
            sumOfPartNumbers += partNumber
        print(sumOfPartNumbers)
