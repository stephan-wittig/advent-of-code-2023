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
    def __init__(self, x: int, y: int, direction: Direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self) -> str:
        return f"({self.x}|{self.y}){self.direction}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Map:
    """Represents the ASCII map given as part of the instructions"""
    def __init__(self, map: str, maxStreak: int) -> None:
        self._map = map.split("\n")
        self.maxStreak = maxStreak

    def getChar(self, x: int, y: int) -> str:
        print(f"Getting {x} {y}")
        if x < 0 or y < 0:
            print("error")
            raise IndexError("Cannot get map char for negative index")
        return self._map[y][x]
    
    def getCost(self, x: int, y: int, direction: Direction, steps: int) -> int:
        """Get cost of move"""
        sum = 0
        for i in range(1, steps + 1):
            xs = x if direction == Direction.vertical else x + i
            ys = y if direction == Direction.horizontal else y + i
            sum += int(self.getChar(xs, ys))
        return sum

    def getNeighbouringNodes(self, n: Node) -> Generator[tuple[Node, int], None, None]:
        """Gets neighbouring nodes and traversal costs, taking movement into account"""

        for d in filter(lambda d: d != n.direction, [Direction.horizontal, Direction.vertical]):
            # Only goes both directions on start field
            for i in [-3, -2, -1, 1, 2, 3]:
                print(f"i:{i}")
                try:
                    cost = self.getCost(n.x, n.y, d, i)
                except IndexError:
                    print("continued")
                    continue # n lies at edge. Neighbour in this direction does not exist
                xs = n.x if d == Direction.vertical else n.x + i
                ys = n.y if d == Direction.horizontal else n.y + i
                yield (Node(
                    xs,
                    ys,
                    d
                ), cost)

    def size(self) -> tuple[int, int]:
        return (len(self._map[-1]), len(self._map))
            
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
        if len(self.tentativeDistances) ==0:
            raise ValueError("Ran out of unvisited nodes!")
        key = min(self.tentativeDistances, key=self.tentativeDistances.get)
        return self.nodes[key]
    
    def findPath(self, start: tuple[int, int], target: tuple[int, int]) -> Generator[Node, None, None]:
        startNode = Node(start[0], start[1], Direction.start)
        self.tentativeDistances[str(startNode)] = 0
        nextNode = startNode
        while nextNode.x != target[0] or nextNode.y != target[1]:
            self.visitNode(nextNode)
            yield nextNode
            nextNode = self.getNextToVisit()
        self.visitNode(nextNode)
        yield nextNode

    def reset(self) -> None:
        self.tentativeDistances.clear()
        self.visited.clear()


cityMap = Map(open("input/day_17.txt").read(), 3)
graph = Graph(cityMap)
for n in cityMap.getNeighbouringNodes(Node(0,0, Direction.start)):
    print(n)

#for i, n in enumerate(graph.findPath((0, 0), (140, 140))):
    #print(f"{n}, d: {graph.confirmedDistances[str(n)]}, i: {i}", file=open('d17.log', 'a'))