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

from hanoi import HanoiTower
from typing import List

def hanoi(start: HanoiTower, end: HanoiTower, temp: List[HanoiTower], n: int):
    pass