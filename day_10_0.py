from typing import List, Tuple, Generator
from math import ceil

class Position:
    """Coordinates of a position on the map. Could also be a vector"""
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"

def addPositions(pos1: Position, pos2: Position) -> Position:
    """Adds two positions, primarily to add a position and a vector"""
    return Position(pos1.x + pos2.x, pos1.y + pos2.y)

def positionsAreEqual(pos1: Position, pos2: Position) -> bool:
    return pos1.x == pos2.x and pos1.y == pos2.y

# Represents a change in coordinates
class Pipe:
    def __init__(self, symbol: str, vector1: Position, vector2: Position) -> None:
        self.vectors = (vector1, vector2)
        self._symbol = symbol

    def __str__(self) -> str:
        return self._symbol
    
    def getConnectedPositions(self, pos: Position) -> (Position, Position):
        """Takes the pipe's position and returns the two connected positions"""
        return (addPositions(pos, self.vectors[0]), addPositions(pos, self.vectors[1]))

pipes = {
    "|": Pipe("|", Position(0, -1), Position(0, 1)),
    "-": Pipe("-", Position(-1, 0), Position(1, 0)),
    "L": Pipe("L", Position(0, 1), Position(1, 0)),
    "J": Pipe("J", Position(-1, 0), Position(0, 1)),
    "7": Pipe("7", Position(-1, 0), Position(0, -1)),
    "F": Pipe("F", Position(0, -1), Position(1, 0))
}
        
class PipeMap:
    def __init__(self, input: str) -> None:
        lines = input.split("\n")
        self._map: List[str] = []
        # lines are parsed in reverse to make indexing more intuitive
        for i in range(len(lines) - 1, -1, -1):
            self._map.append(lines[i])

    def __str__(self) -> str:
        reversedYMap = self._map[::-1]
        return "\n".join(reversedYMap)

    def getSymbol(self, pos: Position) -> str:
        return self._map[pos.y][pos.x]

    def getPipe(self, pos: Position) -> Pipe:
        """Gets pipe at position or error if it's not a pipe"""
        if self.getSymbol(pos) in pipes:
            return pipes[self.getSymbol(pos)]
        raise ValueError(f"'{str(self.getSymbol(pos))}' at {str(pos)} is not a pipe!")
    
    def getStart(self) -> Position:
        """Gets starting position S"""
        for y, line in enumerate(self._map):
            x = line.find("S")
            if x >= 0:
                return Position(x, y)
            
    def getConnectedNeighbours(self, pos: Position):
        """Gets list of pipes pointing to this position, primarily for starting from S"""
        connectedPositions: List[Position] = []
        for c in [(0, -1),(-1, 0),(0, 1),(1, 0)]:
            position = Position(*c)
            try:
                pipePos = addPositions(position, pos)
                pipe = self.getPipe(pipePos)
                connectedPos = pipe.getConnectedPositions(pipePos)
                if positionsAreEqual(connectedPos[0], pos) or positionsAreEqual(connectedPos[1], pos):
                    connectedPositions.append(pipePos)
            except ValueError:
                continue
        return connectedPositions
    
    def traversePipeSegment(self, currentPos: Position, pipePos: Position) -> Position:
        """Traverses one pipe segment at pipePos from currentPos, returning next Position"""
        pipe = self.getPipe(pipePos)
        connectedPositions = pipe.getConnectedPositions(pipePos)
        return connectedPositions[1 if positionsAreEqual(connectedPositions[0], currentPos) else 0]
    
    def traverseCompletePipe(self, reverse = False) -> Generator[Position, None, None]:
        """Crawls through the entire pipe, stopping just before S. Yields the position at every step"""
        previousPos = self.getStart()
        yield previousPos # Yield start as step 0
        possibleCurrentPos = self.getConnectedNeighbours(previousPos)
        if len(possibleCurrentPos) != 2:
            raise ValueError(f"S is not connected to two pipes but to {len(possibleCurrentPos)}")
        currentPos = possibleCurrentPos[int(reverse)]

        # Loop until S is the next Symbol
        while self.getSymbol(currentPos) != "S":
            yield currentPos
            nextPos = self.traversePipeSegment(previousPos, currentPos)
            previousPos = currentPos
            currentPos = nextPos

input = open('input/day_10.txt').read()

pipeMap = PipeMap(input)

pipeLength = 0

for i, pos in enumerate(pipeMap.traverseCompletePipe()):
    print(f"{pos} - step {i}")
    pipeLength = i

print(f"Farthest point is {ceil(pipeLength / 2)} steps away")