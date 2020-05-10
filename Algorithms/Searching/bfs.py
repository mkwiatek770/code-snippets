"""
Depth first search

- using Queue data structure
- FIFO

uses: check if path exists beetween nodes, 
finding "hops" or distance out or "levels" away

Goes Wide
"""
from typing import TypeVar, Generic, Collection, Optional

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

if __name__ == "__main__":
    q = Queue([1, 2, 3, 4])
    q.push(5)
    assert q.pop() == 1
    assert q.pop() == 2
