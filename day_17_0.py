from enum import Enum
from typing import Generator

class Direction(Enum):
    horizontal = "h"
    vertical = "v"
    start = "s"

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return self.__str__()

class Node:
    """Represents one node in the graph"""
    def __init__(self, x: int, y: int, direction: Direction, streak: int) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.streak = streak

    def __str__(self) -> str:
        return f"({self.x}|{self.y})_{self.direction}:{self.streak}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Map:
    """Represents the ASCII map given as part of the instructions"""
    def __init__(self, map: str, maxStreak: int) -> None:
        self._map = map.split("\n")
        self.maxStreak = maxStreak

    def getChar(self, x: int, y: int) -> str:
        if x < 0 or y < 0:
            raise IndexError("Cannot get map char for negative index")
        return self._map[y][x]

    def getNeighbouringNodes(self, n: Node) -> Generator[tuple[Node, int], None, None]:
        """Gets neighbouring nodes and traversal costs, taking movement into account. Note this will also return the previously visited node"""

        possibleMovements: list[tuple[int, int, Direction]] = [
            (1, 0, Direction.horizontal),
            (-1, 0, Direction.horizontal),
            (0, 1, Direction.vertical),
            (0, -1, Direction.vertical)
        ]

        if n.streak >= self.maxStreak:
            possibleMovements = filter(lambda m: m[2] != n.direction, possibleMovements)

        for movement in possibleMovements:
            try:
                cost = int(self.getChar(n.x + movement[0], n.y + movement[1]))
            except IndexError:
                continue # n lies at edge. Neighbour in this direction does not exist
            yield (Node(
                n.x + movement[0],
                n.y + movement[1],
                movement[2],
                n.streak + 1 if n.direction == movement[2] else 1
            ), cost)
            
class Graph:
    """Graph for pathfinding algorithm"""
    edges: dict[str, dict[str, int]] = {}
    nodes: dict[str, Node] = {}
    tentativeDistances: dict[str, int] = {}
    confirmedDistances: dict[str, int]= {}

    def __init__(self, cityMap: Map) -> None:
        self._map = cityMap

    def visitNode(self, n: Node) -> None:
        # Mark node as visited
        currentDistance = self.tentativeDistances[str(n)]
        self.tentativeDistances.pop(str(n))
        self.confirmedDistances[str(n)] = currentDistance

        for nn, cost in self._map.getNeighbouringNodes(n):

            if str(nn) in self.confirmedDistances:
                # Skip if neighbour was visited
                continue
            
            newTentativeDistance = cost + currentDistance

            if not str(nn) in self.nodes:
                # Add to nodes if it wasn't discovered before
                self.nodes[str(nn)] = nn
                self.tentativeDistances[str(nn)] = newTentativeDistance
                continue

            if newTentativeDistance < self.tentativeDistances[str(nn)]:
                # Overwrite distance if new is smaller
                self.tentativeDistances[str(nn)] = newTentativeDistance

    def getNextToVisit(self) -> Node:
        """Get next node to visit. That is the node with lowest tentative distance"""
        key = min(self.tentativeDistances, key=self.tentativeDistances.get)
        return self.nodes[key]
    
    def findPath(self, start: tuple[int, int], target: tuple[int, int]) -> Generator[Node, None, None]:
        startNode = Node(start[0], start[1], Direction.start, 0)
        self.tentativeDistances[str(startNode)] = 0
        nextNode = startNode
        while nextNode.x != target[0] or nextNode.y != target[1]:
            self.visitNode(nextNode)
            yield nextNode
            nextNode = self.getNextToVisit()
        self.visitNode(nextNode)
        yield nextNode

    def reset(self) -> None:
        tentativeDistances = {}
        visited = {}


cityMap = Map(open("input/day_17.txt").read(), 3)
graph = Graph(cityMap)
for i, n in enumerate(graph.findPath((0, 0), (12, 12))):
    print(f"{n}, d: {graph.confirmedDistances[str(n)]}, i: {i}")