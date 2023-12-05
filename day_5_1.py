import re

class MapEntry:
    categoryFrom: str
    categoryTo: str
    startFrom = 0
    startTo = 0
    length = 0

    def __init__(self, categoryFrom: str, categoryTo: str):
        self.categoryFrom = categoryFrom
        self.categoryTo = categoryTo

    def __str__(self) -> str:
        return f"{self.categoryFrom} -> {self.categoryTo}: {self.startFrom} -> {self.startTo}, {self.length}"

input = open('input/day_5.txt').read()

seedsMatch = re.search("^seeds: ([\d ]+)$", input, flags=re.MULTILINE)
if seedsMatch == None:
    raise ValueError("Invalid format of seeds list")

seedsInput = list(map(lambda n: int(n), seedsMatch.group(1).split(" ")))

seedsRanges = []
for i in range(0, len(seedsInput) - 1, 2):
    seedsRanges.append((seedsInput[i], seedsInput[i] + seedsInput[i + 1]))

def inRange(n: int):
    for r in seedsRanges:
        if n >= r[0] and n < r[1]:
            return True
    return False

print(f"Seeds ranges: {seedsRanges}")
print("=== Finished parsing seeds")

pos = seedsMatch.end()

mapRe = re.compile("(\w+)-to-(\w+) map:\n((?:[\d ]+\n?))+")
mapEntryRe = re.compile("^(\d+) (\d+) (\d+)$", flags = re.MULTILINE)
mapEntries = []

# Parse all maps and map entries
while pos + 1 <= len(input):
    mapMatch = mapRe.search(input, pos)
    if mapMatch == None:
        break
    for mapEntryMatch in mapEntryRe.finditer(input, mapMatch.start(), mapMatch.end()):
        newMapEntry = MapEntry(mapMatch.group(1), mapMatch.group(2))
        newMapEntry.startTo = int(mapEntryMatch.group(1))
        newMapEntry.startFrom = int(mapEntryMatch.group(2))
        newMapEntry.length = int(mapEntryMatch.group(3))
        print(newMapEntry)
        mapEntries.append(newMapEntry)
    pos = mapMatch.end()

print("=== Finished parsing maps")



def reverseMapSeed(location):
    currentCategory = "location"
    currentNumber = location

    while currentCategory != "seed":
        filteredMEs = list(filter(lambda me: me.categoryTo == currentCategory, mapEntries))
        currentCategory = filteredMEs[0].categoryFrom
        for me in filteredMEs:
            if currentNumber >= me.startTo and currentNumber < me.startTo + me.length:
                currentNumber = currentNumber - me.startTo + me.startFrom
                break
            # if not found in any map entry, s stays the same
    print(f"Location, Seed: {location}: {currentNumber}")
    return currentNumber

i = 0

while True:
    seed = reverseMapSeed(i)
    if inRange(seed):
        break
    i += 10000

j = i - 9999

while j < i:
    seed = reverseMapSeed(j)
    if inRange(seed):
        print(f"Lowest Seed:Location Pair in range found: {seed}:{j}")
        break
    j += 1
    