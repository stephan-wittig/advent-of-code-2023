import re
from enum import Enum
from collections import Counter
from functools import cmp_to_key, reduce

lines = open('input/day_7.txt').read().split('\n')

class Type(Enum):
    FIVE = 6
    FOUR = 5
    FULLHOUSE = 4
    THREE = 3
    TWOPAIRS = 2
    ONEPAIR = 1
    SINGLE = 0

symbols = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

class Hand:
    def __calcType(self):
        c = Counter(self.cards)
        mostCommon = c.most_common(None)
        mostCommonJ = list(filter(lambda x: x[0] == "J", mostCommon))
        numOfJ = mostCommonJ[0][1] if mostCommonJ else 0
        mostCommon = list(filter(lambda x: x[0] != "J", mostCommon))
        print(f"{numOfJ} {mostCommon}")

        match (mostCommon[0][1] if mostCommon else 0) + numOfJ:
            case 5:
                return Type.FIVE
            case 4:
                return Type.FOUR
            case 3:
                if mostCommon[1][1] == 2:
                    return Type.FULLHOUSE
                return Type.THREE
            case 2:
                if mostCommon[1][1] == 2:
                    return Type.TWOPAIRS
                return Type.ONEPAIR
            case _:
                return Type.SINGLE

    def __init__(self, line: str) -> None:
        m = re.match("(\w{5}) (\d+)", line)
        if m == None:
            raise ValueError("Cannot parse hand")
        self.cards = m.group(1)
        self.bid = int(m.group(2))
        self.type = self.__calcType()

    def __str__(self) -> str:
        return f"{self.cards} {self.bid} {self.type.name}"

# 0 for equal, -1 if h2 is wins, 1 if h1 wins
def cmpHands(h1: Hand, h2: Hand):
    if h1.cards == h2.cards:
        return 0

    if h1.type.value > h2.type.value:
        return 1
    
    if h1.type.value < h2.type.value:
        return -1
    
    for i in range(len(h1.cards)):
        c1 = symbols.index(h1.cards[i])
        c2 = symbols.index(h2.cards[i])

        if c1 < c2:
            return 1
        
        if c1 > c2:
            return -1
    
    return 0

hands = map(Hand, lines)
sortedHands = sorted(hands, key=cmp_to_key(cmpHands))
print("\n".join(map(str, sortedHands)))

winnings = 0
for i, hand in enumerate(sortedHands):
    winnings += (i + 1) * hand.bid
print(f"Winnings: {winnings}")
