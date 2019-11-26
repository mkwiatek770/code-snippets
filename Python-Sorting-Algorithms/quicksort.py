

def swap(l: list, index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp

def quicksort(unsorted: list, start, end) -> list:
    if start == end:
        return [unsorted[start]]
    
    pivot = unsorted[end]
    j = 0
    for i in range(start, end):
        if unsorted[i] < pivot:
            swap(unsorted, i, j)
            j += 1
    swap(unsorted, j, end)

    left = quicksort(unsorted, start, j - 1)
    right = quicksort(unsorted, j + 1, end)
    return left + [pivot] + right

    
print(quicksort([10, 7, 12, 8, 3, 2, 6], 0, 6))
