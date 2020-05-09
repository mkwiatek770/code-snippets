"""
Depth first search

- using Stack data structure
- LIFO

uses: backtracking, complete search, exhausting possible paths

Goes Wide

Time: O(|V| + |E|)
Space: O(|V|)
V - vertices
E - edges
"""
from typing import TypeVar, List, Generic, Set

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []
    
    @property
    def empty(self):
        return len(self._container) == 0

    def pop(self) -> T:
        if not self.empty:
            return self._container.pop()

    def push(self, item: T) -> None:
        self._container.append(item)

class Node:
    def __init__(self, value: T):
        self.value = value
        self.adjacent: List[Node] = []


def dfs(start_node: Node) -> None:
    """Dfs which print all visited nodes."""
    stack = Stack()
    explored: Set[Node] = set()
    stack.push(start_node)

    while not stack.empty:
        current = stack.pop()
        if current not in explored:
            print(f"{current.value}")
            explored.add(current)

        for neighbour in current.adjacent:
            if neighbour not in explored:
                stack.push(neighbour)


if __name__ == "__main__":
    stack = Stack()
    stack.push(123)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == 123

    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    G = Node('G')
    F = Node('F')
    H = Node('H')

    C.adjacent = [B, D, E, F]
    B.adjacent = [A, D, C]
    A.adjacent = [G, B]
    H.adjacent = [G, E]
    G.adjacent = [A, H, F]
    D.adjacent = [B, C, E]
    E.adjacent = [C, D, H, F]
    F.adjacent = [G, C, E]

    dfs(C)
