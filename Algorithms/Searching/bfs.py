"""
Depth first search

- using Queue data structure
- FIFO

uses: check if path exists beetween nodes, 
finding "hops" or distance out or "levels" away

Goes Wide
"""
from typing import TypeVar, Generic, Collection, Optional, Set
from dfs import Node

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self, container: Collection[T] = None):
        if container:
            self._container = list(container)
        else:
            self._container = []
    
    @property
    def empty(self):
        return len(self._container) == 0

    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> Optional[T]:
        if not self.empty:
            return self._container.pop(0)


def bfs(start_node: Node) -> None:
    queue = Queue()
    explored: Set[Node] = set()
    queue.push(start_node)

    while not queue.empty:
        current = queue.pop()
        if current not in explored:
            print(current.value)
            explored.add(current)
        for adj in current.adjacent:
            if adj not in explored:
                queue.push(adj)


if __name__ == "__main__":
    
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    G = Node('G')
    F = Node('F')
    H = Node('H')

    A.adjacent = [B, C, D, E]
    B.adjacent = [A, G, C]
    C.adjacent = [A, B, D]
    D.adjacent = [C, H, E, A]
    E.adjacent = [F, A, D]
    G.adjacent = [F, B]
    H.adjacent = [F, D]
    F.adjacent = [H, E, G]

    bfs(A)
