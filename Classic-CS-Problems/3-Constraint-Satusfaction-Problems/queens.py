from typing import List, Dict, Optional
from csp import CSP, Constraint


class QueensConstraint(Constraint[int, int]):

    def __init__(self, columns: List[int]) -> None:
        super().__init__(columns)
        self.columns: List[int] = columns
    
    def satisfied(self, assignment: Dict[int, int]):
        # q1c = queen 1 column, q1r = queen 1 row
        for q1c, q1r in assignment.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r: # same row
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): # same diagonal
                        return False
        return True



if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {i: columns for i in range(8)}
    csp: CSP[int, int] = CSP(columns, rows)
    
