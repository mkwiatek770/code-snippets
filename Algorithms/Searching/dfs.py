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
from typing import TypeVar, List

T = TypeVar('T')

class Stack:

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


if __name__ == "__main__":
    stack = Stack()
    stack.push(123)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == 123
