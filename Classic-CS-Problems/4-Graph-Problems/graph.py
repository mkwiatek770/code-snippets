from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = None) -> None:
        self._vertices: List[V] = list(vertices) if vertices else []
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    def index_of(self, vertex: V) -> int:
        try:
            return self._vertices.index(vertex)
        except ValueError:
            return -1

    def neighbours_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbours_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbours_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbours_for_index(i)}\n"
        return desc

# def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
#     frontier: Queue[Node[T]] = Queue()
#     frontier.push(Node(initial, None))

#     explored: Set[T] = {initial}

#     while not frontier.empty:
#         current_node: Node[T] = frontier.pop()
#         current_state: T = current_node.state

#         if goal_test(current_state):
#             return current_node
#         for child in successors(current_state):
#             if child in explored:
#                 continue
#             explored.add(child)
#             frontier.push(Node(child, current_node))
#     return None


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", 
    "Riverside", "Phoenix", "Chicago", "Boston", "New York",
    "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
    "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)

    import sys
    sys.path.insert(0, '..')
    import importlib
    module = importlib.import_module('2-Search-Problems.generic_search')
    bfs = module.bfs
    Node = module.Node
    node_to_path = module.node_to_path

    bfs_result: Optional[Node[V]] = bfs("Boston", lambda x: x == "Miami", city_graph.neighbours_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search.")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Path from Boston to Miami:")
        print(path)