"""
Show the performance advantage of binary search over linear search by creating
a list of one million numbers and timing how long it takes the linear_
contains() and binary_contains() functions defined in this chapter to find
various numbers in the list.
"""
import unittest
import time
from typing import List
from generic_search import linear_contains, binary_contains


class TestSearchPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.long_list: List[int] = [i for i in range(1_000_000)]
    
    def test_linear_search_item_exist(self):

        # test easy case
        t0 = time.perf_counter()
        res = linear_contains(self.long_list, 1000)
        t1 = time.perf_counter()
        print(f"To find item 1000 it took {t1-t0} secs")
        self.assertTrue(res)
        
        # test average case
        t0 = time.perf_counter()
        res = linear_contains(self.long_list, 500_000)
        t1 = time.perf_counter()
        print(f"To find item 500000 it took {t1-t0} secs")
        self.assertTrue(res)

        # test worst case
        t0 = time.perf_counter()
        res = linear_contains(self.long_list, 999999)
        t1 = time.perf_counter()
        print(f"To find item 999999 it took {t1-t0} secs")
        self.assertTrue(res)

        # test non existing item
        t0 = time.perf_counter()
        res = linear_contains(self.long_list, -1)
        t1 = time.perf_counter()
        print(f"To find item -1 it took {t1-t0} secs")
        self.assertFalse(res)
    
    def test_binary_search(self):

        # test easy case
        t0 = time.perf_counter()
        res = binary_contains(self.long_list, 500_000)
        t1 = time.perf_counter()
        print(f"To find item 1000 it took {t1-t0} secs")
        self.assertTrue(res)

        # test hard case
        t0 = time.perf_counter()
        res = binary_contains(self.long_list, 500_001)
        t1 = time.perf_counter()
        print(f"To find item 500_001 it took {t1-t0} secs")
        self.assertTrue(res)

        # test non existing item
        t0 = time.perf_counter()
        res = binary_contains(self.long_list, -1)
        t1 = time.perf_counter()
        print(f"To find item -1 it took {t1-t0} secs")
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()