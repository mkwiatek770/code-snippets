"""
- Inplace sorting

Best: O(n) / O(nlogn)
Average: O(nlogn)
Worst: O(nlogn)
"""

# iParent(i)     = floor((i-1) / 2) where floor functions map a real number to the smallest leading integer.
# iLeftChild(i)  = 2*i + 1
# iRightChild(i) = 2*i + 2

def heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    print(heap_sort([ 12, 11, 13, 5, 6, 7]))

