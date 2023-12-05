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

seeds = list(map(lambda n: int(n), seedsMatch.group(1).split(" ")))
print(f"seeds: {seeds}")
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

currentCategory = "seed"
state = seeds

while currentCategory != "location":
    print(f"=== Mapping from {currentCategory}")
    filteredMEs = list(filter(lambda me: me.categoryFrom == currentCategory, mapEntries))
    currentCategory = filteredMEs[0].categoryTo

    for i, s in enumerate(state):
        for me in filteredMEs:
            if s >= me.startFrom and s < me.startFrom + me.length:
                state[i] = s - me.startFrom + me.startTo
                break
            # if not found in any map entry, s stays the same
        print(f"{s} -> {state[i]}")

print("=== Finished mapping")
print(state)
print(f"Smallest location: {min(state)}")