input = open('input/day_2.txt').read().split('\n')
games = []
for line in input:
    r = line.split(": ")
    id = r[0]
    nId=int(id.split(" ")[1])
    samples = r[1].split("; ")
    pSamples = []
    for sample in samples:
        elements = sample.split(", ")
        pSample = {}
        for element in elements:
            v = element.split(" ")
            pSample[v[1]] = int(v[0])
        pSamples.append(pSample)
    games.append({
        "id": nId,
        "samples": pSamples
    })


sumOfPowers = 0


def getMinCubes(game: dict):
    minCubes = {"red": 0, "green": 0, "blue": 0}
    for sample in game["samples"]:
        for k, v in sample.items():
            minCubes[k] = max((minCubes[k], v))
    print(minCubes)
    return minCubes

for i, game in enumerate(games):
    minCubes = getMinCubes(game)
    power = 1
    for min in minCubes.values():
        power *= min
    games[i]["power"] = power
    sumOfPowers += power

print(games)
print(sumOfPowers)