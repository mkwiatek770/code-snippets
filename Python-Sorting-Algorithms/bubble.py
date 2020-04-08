"""
Bubble Sort

Simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Best Case: O(n) 
Average: O(n^2)
Worst Case: O(n^2)
"""


def bubble(unsorted: list) -> list:
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                swaps = True
    return unsorted


# Better way
def bubble(collection):
    for crossing in range(len(collection) - 1):
        for i in range(len(collection) - crossing -1):
            first = collection[i]
            second = collection[i + 1]
            if first > second:
                collection[i], collection[i+1] = collection[i+1], collection[i]
    return collection



if __name__ == "__main__":
    start = [5, 1, 4, 8, 2]
    print("Start array: ", start)
    print("Result: ", bubble(start))
