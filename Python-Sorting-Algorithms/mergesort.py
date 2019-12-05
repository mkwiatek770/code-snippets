
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


merge([1, 2], [4, 5])

