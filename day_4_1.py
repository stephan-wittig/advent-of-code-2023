import re

input = open('input/day_4.txt').read().split('\n')

class Scratchcard:
    instances = 1
    score = 0

    def __init__(self, score: int):
        self.score = score

    def incInstances(self, n: int):
        self.instances += n

    def __str__(self) -> str:
        return(f"n: {self.instances}, s: {self.score}")

totalNumberOfCards = 0
cards = []
for line in input:
    match = re.search("Card +\d+: +([\d ]+) \| +([\d ]+)", line)
    if match == None:
        raise ValueError("Invalid input format")
    winNos = list(map(lambda str: int(str),re.split("\s+", match.group(1))))
    yourNos = list(map(lambda str: int(str),re.split("\s+", match.group(2))))
    winningNos = list(filter(lambda no: winNos.count(no) > 0, yourNos))
    score = len(winningNos)
    cards.append(Scratchcard(score))

for i, card in enumerate(cards):
    print(card)
    totalNumberOfCards += card.instances
    for j in range(i, i + card.score):
        if j + 2 > len(cards):
            continue

        cards[j + 1].incInstances(card.instances)

print(totalNumberOfCards)