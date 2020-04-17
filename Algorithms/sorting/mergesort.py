"""
Merge sort
divide collection into parts and then merge then

Its efficient, but downside is than it requires extra space
"""


def merge(arr1: list, arr2: list) -> list:
    new_arr = []
    for i in arr1:
        for j in arr2:
            if j < i:
                new_arr.append(j)
                arr2.remove(j)
            else:
                new_arr.append(i)
                arr1.remove(i)
    return new_arr



def mergesort(arr: list):
    if len(arr) == 1:
        return arr

    first_half = arr[:len(arr) // 2]
    second_half = arr[len(arr) // 2:]
    
    res1 = mergesort(first_half)
    res2 = mergesort(second_half)
    return res1, res2


print(mergesort([1, 2, 3, 4, 5]))
print(mergesort([1, 2, 3, 4]))

#merge([1, 2], [4, 5])

