"""
Add a counter to dfs(), bfs(), and astar() to see how many states each
searches through for the same maze. Find the counts for 100 different mazes to
get statistically significant results.
"""
from typing import TypeVar, Callable, List, Optional, Set, Tuple
from generic_search import Node, Queue, node_to_path, Stack
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


def dfs_w_counter(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Tuple[Optional[Node[T]], int]:
    counter = 0
    # frontier is where we've yet to go
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # explored is where we've been
    explored: Set[T] = {initial}

    # keep going while there is more to explore
    while not frontier.empty:
        counter += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # if we found the goal, we're done
        if goal_test(current_state):
            return current_node, counter
        # check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None, counter # went through everything and never found goal


if __name__ == "__main__":
    maze: Maze = Maze()

    # Test DFS
    solution1, counter = dfs_w_counter(maze.start, maze.goal_test, maze.successors)
    print(f"Counter: {counter}")
    if solution1 is None:
        print("No solutions found using depth-first search.")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)
    
    # Test BFS
    solution2, counter = bfs_w_counter(maze.start, maze.goal_test, maze.successors)
    print(f"Counter: {counter}")
    if solution2 is None:
        print("No solution found using breadth-first search!")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        maze.mark(path2)
        print(maze)
        maze.clear(path2)