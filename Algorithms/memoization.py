from typing import Dict
from functools import lru_cache

# normal fibbonaci nth element function
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# self made memoization
memo: Dict[int, int] = {0: 0, 1: 1} # base cases
def fib(n: int):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n] 


# great lru_cache library
@lru_cache()
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


