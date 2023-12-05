import re
import logging
logging.basicConfig(filename='day5.log', encoding='utf-8', level=logging.DEBUG)

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
seeds = []
for i in range(0, len(seedsInput) - 1, 2):
    logging.debug(f"Adding seeds {seedsInput[i]} - {seedsInput[i] + seedsInput[i + 1]}")
    for j in range(seedsInput[i], seedsInput[i] + seedsInput[i + 1]):
        seeds.append(j)


logging.debug(f"Expanded to {len(seeds)} seeds")
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
        logging.debug(newMapEntry)
        mapEntries.append(newMapEntry)
    pos = mapMatch.end()

print("=== Finished parsing maps")

def mapSeedToLocation(s):
    currentCategory = "seed"
    t = s
    while currentCategory != "location":
        filteredMEs = list(filter(lambda me: me.categoryFrom == currentCategory, mapEntries))
        nextCategory = filteredMEs[0].categoryTo

        for me in filteredMEs:
            if s >= me.startFrom and s < me.startFrom + me.length:
                t = s - me.startFrom + me.startTo
            # if not found in any map entry, s stays the same
        print(f"{currentCategory} -> {nextCategory} {s} -> {t}")
        currentCategory = nextCategory
        s = t
    return s

locationsMap = map(mapSeedToLocation, seeds)
locationsList = list(locationsMap)
print("=== Finished mapping")

print(f"Smallest location: {min(locationsList)}")