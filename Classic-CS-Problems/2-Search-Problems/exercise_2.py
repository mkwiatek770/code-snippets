"""
Add a counter to dfs(), bfs(), and astar() to see how many states each
searches through for the same maze. Find the counts for 100 different mazes to
get statistically significant results.
"""
from typing import TypeVar, Callable, List, Optional
from generic_search import Node, Queue

T = TypeVar('T')


def bfs_w_counter(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Tuple[Optional[Node[T]], int]:
    counter = 0
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    
    explored: Set[T] = {initial}

    while not frontier.empty:
        counter += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node, counter
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None, counter

