instructions = open("input/day_15.txt").read().split(",")

def hash(input: str) -> int:
    value = 0
    for c in input:
        value += ord(c)
        value = value * 17
        value = value % 256
    return value

result = sum([hash(i) for i in instructions])
print(result)