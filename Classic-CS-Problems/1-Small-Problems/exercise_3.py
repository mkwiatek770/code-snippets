""""
Write a solver for The Towers of Hanoi that works for any number of towers.
"""


"""
 Frame–Stewart algorithm

* Let n be the number of disks.
* Let r be the number of pegs.
* Define T(n,r) to be the minimum number of moves required to transfer n disks using r pegs.

1. For some k, 1 <= k < n  transfer top k disks to a single peg other than detination pegs, taking T(k, n) moves
2. Without disturbing the peg that now contains the top k disks, transfer the remaining n-k disks to the destination
peg using only remaining r-1 pegs, taking T(n-k, r-1) moves.
3. Finally transfer the top k disks to the destination peg, taking T(k,r) moves

https://codereview.stackexchange.com/questions/42524/solving-the-reves-puzzle/42527
"""
from typing import List
from hanoi import HanoiTower



def frame_steward(start: HanoiTower, end: HanoiTower, other_pegs: List[HanoiTower]):
    
    # For some k, 1 <= k < n  transfer top k disks to a single peg other than detination pegs, taking T(k, n) moves
    temp_destination = other_pegs.pop()
    k = len(other_pegs)
    hanoi(start, temp_destination, other_pegs, k)

    print(start)
    print(temp_destination)

    #Without disturbing the peg that now contains the top k disks, transfer the remaining n-k disks to the destination
    # peg using only remaining r-1 pegs, taking T(n-k, r-1) moves.
    hanoi(start, end, other_pegs, len(start._container))
    
    print(start)
    print(end)

    # Finally transfer the top k disks to the destination peg, taking T(k,r) moves
    hanoi(temp_destination, end, other_pegs, k)
    
    print(start)
    print(end)

def hanoi(start: HanoiTower, end: HanoiTower, temp: List[HanoiTower], n: int):
    for i in range(n):
        temp[i].push(start.pop())

    for i in range(n - 1, -1, -1):
        end.push(temp[i].pop())


h1 = HanoiTower('A', initial=[5, 4, 3, 2, 1])
h2 = HanoiTower('B')
h3 = HanoiTower('C')
h4 = HanoiTower('D')
h5 = HanoiTower('E')
h6 = HanoiTower('F')
h7 = HanoiTower('G')

frame_steward(h1, h7, [h2, h3, h4, h5, h6])