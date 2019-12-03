"""
Quick sort

Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined.

Best Case: O(n*log(n)) 
Average: O(n*log(n))
Worst Case: O(n^2)
"""


def swap(l: list, index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp


def partition(arr: list, start, end):
    pivot = arr[end]
    j = start
    for i in range(start, end):
        if arr[i] < pivot:
            swap(arr, i, j)
            j += 1
    swap(arr, j, end)
    return j


def quicksort(unsorted: list, start, end) -> list:

    if start >= end:
        return

    p = partition(unsorted, start, end)
    quicksort(unsorted, start, p - 1)
    quicksort(unsorted, p + 1, end)

    return unsorted


if __name__ == "__main__":
    print(quicksort([10, 7, 12, 8, 3, 2, 6], 0, 6))
