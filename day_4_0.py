import re

input = open('input/day_4.txt').read().split('\n')

totalScore = 0

for line in input:
    match = re.search("Card +\d+: +([\d ]+) \| +([\d ]+)", line)
    if match == None:
        raise ValueError("Invalid input format")
    winNos = list(map(lambda str: int(str),re.split("\s+", match.group(1))))
    yourNos = list(map(lambda str: int(str),re.split("\s+", match.group(2))))
    winningNos = list(filter(lambda no: winNos.count(no) > 0, yourNos))
    if len(winningNos) > 0:
        score = 2 ** (len(winningNos) - 1 )
        print(score)
        totalScore += score

print(totalScore)