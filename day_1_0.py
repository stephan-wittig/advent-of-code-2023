import re

input = open('input/day_1.txt').read().split('\n')

def  processLine(line: str):
    matches = re.findall("(\d)", line)

    if len(matches) < 1:
        raise ValueError("Line does not contain digits!")
    
    sNumber = matches[0] + matches[-1]
    return int(sNumber)

print(sum(map(processLine, input)))
