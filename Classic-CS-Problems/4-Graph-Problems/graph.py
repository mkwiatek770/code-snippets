from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = None) -> None:
        self._vertices: List[V] = list(vertices) if vertices else []
        self._edges: List[List[Edge]] = [[] for _ in vertices]