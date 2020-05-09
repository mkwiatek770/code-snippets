"""
Only works on sorted collection

Best Case: O(1)
Average Case: O(logn)
Worst Case: O(logn)
"""


def binary_search(arr: list, target):
    """
    Collection has to be sorted!
    Returns False if element was not found.
    """
    if len(arr) == 0:
        return False

    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            return m
    return False


if __name__ == "__main__":
    assert binary_search([2, 4, 6, 7, 8], 6) == 2
    assert binary_search([12, 16, 18], 18) == 2
    assert binary_search([2, 3, 5], 2) == 0
    assert binary_search([2, 7, 11], 123) == False
    
