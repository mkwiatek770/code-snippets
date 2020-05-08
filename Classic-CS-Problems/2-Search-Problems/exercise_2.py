"""
Add a counter to dfs(), bfs(), and astar() to see how many states each
searches through for the same maze. Find the counts for 100 different mazes to
get statistically significant results.
"""
from typing import TypeVar, Callable, List, Optional, Set, Tuple
from generic_search import Node, Queue, node_to_path
from maze import Maze, MazeLocation

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


if __name__ == "__main__":
    maze: Maze = Maze()

    # Test DFS
    solution1, counter = bfs_w_counter(maze.start, maze.goal_test, maze.successors)
    print(f"Counter: {counter}")
    if solution1 is None:
        print("No solutions found using depth-first search.")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)