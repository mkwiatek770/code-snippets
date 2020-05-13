"""
A* Search

A* score = cost + heuristic
"""
from __future__ import annotations
from heapq import heappop, heappush
from typing import TypeVar, Generic, Collection, Optional, Callable, List, Optional

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    def __init__(self, container: Optional[Collection[T]] = None):
        if container:
            self._container = list(container)
        else:
            self._container = []
    
    def __repr__(self):
        return f'PriorityQueue(repr({self._container}))'
    
    @property
    def empty(self):
        return len(self._container) == 0

    def push(self, item: T) -> None:
        heappush(self._container, item)
    
    def pop(self) -> T:
        return heappop(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.parent: Optional[Node] = parent
        self.state: T = state
        self.cost: float = cost
        self.heuristic: float = heuristic
    
    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def astar(initial: Node[T], goal_test: Callable[[T], bool], successors: Callable[[T], 
        List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier = PriorityQueue()
    frontier.push(initial)

    explored = {initial: 0.0}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None

if __name__ == '__main__':
    queue = PriorityQueue([2, 4, 6, 1])
    print(queue.pop())
    queue.push(12)
    print(queue.pop())
