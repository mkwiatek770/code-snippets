"""
Write yet another function that solves for element n of the Fibonacci sequence, using a technique of your own design. 
Write unit tests that evaluate its correctness and performance relative to the other versions in this chapter.
"""
import time
import unittest


def fibbonaci(n: int) -> int:
    if n < 2:
        return n
    first = 1
    second = 1
    for _ in range(n - 2):
        first, second = first + second, first
    return first

def fibbonaci_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibbonaci_recursive(n - 1) + fibbonaci_recursive(n - 2)


class TestFibbonaci(unittest.TestCase):

    def test_fibbonaci(self):
        self.assertEqual(fibbonaci(0), 0)
        self.assertEqual(fibbonaci(2), 1)
        self.assertEqual(fibbonaci(6), 8)
        self.assertEqual(fibbonaci(10), fibbonaci_recursive(10))
    
    def test_performance(self):
        t0 = time.perf_counter()
        res = fibbonaci_recursive(10)
        t1 = time.perf_counter()
        print(f"fibbonaci_recursive(10) took {t1-t0} seconds")
        t0 = time.perf_counter()
        res = fibbonaci(10)
        t1 = time.perf_counter()
        print(f"fibbonaci(10) took {t1-t0} seconds")

        t0 = time.perf_counter()
        res = fibbonaci_recursive(30)
        t1 = time.perf_counter()
        time1 = t1 - t0
        print(f"fibbonaci_recursive(30) took {time1:.4f} seconds")
        t0 = time.perf_counter()
        res = fibbonaci(30)
        t1 = time.perf_counter()
        time2 = t1 - t0
        print(f"fibbonaci(30) took {time2:.4f} seconds")
        print(f"Non recursive version is {time1/time2} faster")

if __name__ == "__main__":
    unittest.main()
    # print(fibbonaci(8))
    # print(fibbonaci(3))
