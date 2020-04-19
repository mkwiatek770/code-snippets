"""
Timsort - standard sorting algorithm in python.

- Hybrid of Merge sort and Insertion sort.
- Stable
- Tim Peters is the author
Visualisation: https://www.youtube.com/watch?v=NVIjHj-lrT4
- If the array we are trying to sort has fewer than 64 elements in it, Timsort will execute an insertion sort.

Best Case: O(n)
Average: O(nlogn)
Worst Case: O(nlogn)
"""
from mergesort import merge
from insertion import insertion

def binary_search(arr: list, target):
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


def timsort(arr):
    runs, sorted_runs = [], []
    length = len(arr)
    if length == 0:
        return arr
    new_run = [arr[0]]

    for i in range(1, length):
        
        if i == length - 1:
            new_run.append(arr[i])
            runs.append(new_run)
            break
        if arr[i] < arr[i - 1]:
            if new_run is None:
                runs.append(new_run)
                new_run = []
            else:
                runs.append([arr[i]])
                new_run.append(arr[i])

        else:
            new_run.append(arr[i])

    for collection in runs:
        sorted_runs.append(insertion(collection))

    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array

if __name__ == "__main__":
    timsort([123, -11, 22, 1, 2, 62]) == [-11, 1, 2, 22, 62, 123]

