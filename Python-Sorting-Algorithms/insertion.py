"""
Insertion sort

Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

Best Case: O(n) 
Average: O(n^2)
Worst Case: O(n^2)
"""


def insertion(unsorted: list) -> list:
    list_len = len(unsorted)
    for i in range(1, list_len):
        for j in range(i):
            if i == j:
                continue
            if unsorted[i] < unsorted[j]:
                val = unsorted.pop(i)
                unsorted.insert(j, val)
    return unsorted


if __name__ == "__main__":
    start = [12, 11, 13, 5, 6]
    print("Start array: ", start)
    print("Result: ", insertion(start))
