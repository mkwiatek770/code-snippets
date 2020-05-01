from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Edge:
    u: int # from vertex
    v: int # to vertex

    def reversed(self):
        return Edge(self.v, self.u)
    
    def __str__(self):
        return f"{self.u} -> {self.v}"
