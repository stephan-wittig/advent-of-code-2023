import regex as re

input = open('input/day_1.txt').read().split('\n')
numbersDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

numbersRegEx = "|".join(numbersDict.keys())

def mapNumber(number: str):
    if len(number) == 1:
        return number;
    newNumber = numbersDict.get(number)
    if newNumber == None:
        raise ValueError("String does not represent a number!")
    return newNumber

def  processLine(line: str):
    matches = re.findall(f"{numbersRegEx}|\d", line, overlapped = True)

    if len(matches) < 1:
        raise ValueError("Line does not contain digits!")
    
    sNumber = mapNumber(matches[0]) + mapNumber(matches[-1])
    
    return int(sNumber)


print(sum(map(processLine, input)))
