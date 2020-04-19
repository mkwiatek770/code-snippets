"""
Merge sort
divide collection into parts and then merge then

Its efficient, but downside is than it requires extra space
"""

def merge(arr1: list, arr2: list) -> list:
    new_arr = []
    # Iterate while at least one array is not empty
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] <= arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    
    # At this point at least one array is empty add leftovers
    new_arr += arr1
    new_arr += arr2

    return new_arr


def mergesort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    first_half = arr[:len(arr) // 2]
    second_half = arr[len(arr) // 2:]
    
    left = mergesort(first_half)
    right = mergesort(second_half)
    
    return merge(left, right)

if __name__ == "__main__":
    print(mergesort([4, -5, 2, 123, 11]))
    print(mergesort([1, 111, 3, -5]))

