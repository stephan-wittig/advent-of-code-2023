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


maxCubes = {"red": 12, "green": 13, "blue": 14}
sumOfPossibleGameId = 0


def isPossibleSample(sample: dict):
    for k, v in sample.items():
        if v > maxCubes[k]:
            return False
    return True

def isPossibleGame(possibleSamples):
    for possibleSample in possibleSamples:
        if not possibleSample:
            return False
    return True

for i, game in enumerate(games):
    possibles = map(isPossibleSample, game["samples"])
    games[i]["possible"] = isPossibleGame(possibles)
    if games[i]["possible"]:
        sumOfPossibleGameId += game["id"]

print(games)
print(sumOfPossibleGameId)