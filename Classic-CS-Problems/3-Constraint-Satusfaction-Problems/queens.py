from typing import List, Dict, Optional
from csp import CSP, Constraint






if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {i: columns for i in range(8)}
    csp: CSP[int, int] = CSP(columns, rows)
