"""
Add a counter to dfs(), bfs(), and astar() to see how many states each
searches through for the same maze. Find the counts for 100 different mazes to
get statistically significant results.
"""
from typing import TypeVar, Callable, List, Optional, Set, Tuple, Dict
from generic_search import Node, Queue, node_to_path, Stack, PriorityQueue
from maze import Maze, MazeLocation, manhattan_distance

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


def astar_w_counter(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]], 
           heuristic: Callable[[T], float]) -> Tuple[Optional[Node[T]], int]:
    
    counter = 0
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None))

    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.empty:
        counter += 1
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node, counter
        
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None, counter


if __name__ == "__main__":

    DFS_COUNTER = 0
    BFS_COUNTER = 0
    ASTAR_COUNTER = 0

    for _ in range(100):
        maze: Maze = Maze()

        # Test DFS
        solution1, counter = dfs_w_counter(maze.start, maze.goal_test, maze.successors)
        print(f"DFS Counter: {counter}")
        if solution1 is None:
            print("No solutions found using depth-first search.")
        else:
            path1: List[MazeLocation] = node_to_path(solution1)
            maze.mark(path1)
            print(maze)
            maze.clear(path1)
        
        DFS_COUNTER += counter

        # Test BFS
        solution2, counter = bfs_w_counter(maze.start, maze.goal_test, maze.successors)
        print(f"BFS Counter: {counter}")
        if solution2 is None:
            print("No solution found using breadth-first search!")
        else:
            path2: List[MazeLocation] = node_to_path(solution2)
            maze.mark(path2)
            print(maze)
            maze.clear(path2)
        BFS_COUNTER += counter

        # Test A*
        distance: Callable[[MazeLocation], float] = manhattan_distance(maze.goal)
        solution3, counter = astar_w_counter(maze.start, maze.goal_test, maze.successors, distance)
        print(f"A* Counter: {counter}")
        if solution3 is None:
            print("No solution found using A*!")
        else:
            path3: List[MazeLocation] = node_to_path(solution3)
            maze.mark(path3)
            print(maze)
        ASTAR_COUNTER += counter

    print("Average results after 100 iterations:")
    print(f"BFS:  {BFS_COUNTER // 100} steps per maze")
    print(f"DFS:  {DFS_COUNTER // 100} steps per maze")
    print(f"A*:   {ASTAR_COUNTER // 100} steps per maze")
