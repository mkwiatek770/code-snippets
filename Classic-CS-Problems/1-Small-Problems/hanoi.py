from typing import TypeVar, Generic, List, Optional
T = TypeVar("T")

class Stack(Generic[T]):
    """LIFO Stack"""
    def __init__(self, initial: Optional[List[T]] = None) -> None:
        if initial:
            self._container = list(initial)
        else:
            self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)


class HanoiTower(Stack[int]):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n) -> None:
    print(f"hanoi(begin={begin.name}, end={end.name}, temp={temp.name}, n={n})")
    if n == 1:
        print(f"Move element from {begin.name} to {end.name}")
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":

    num_discs: int = 10
    tower_a: HanoiTower = HanoiTower('A')
    tower_b: HanoiTower = HanoiTower('B')
    tower_c: HanoiTower = HanoiTower('C')
    for i in range(1, num_discs + 1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)