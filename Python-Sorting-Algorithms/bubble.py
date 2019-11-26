"""
Bubble Sort

Simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

Best Case: O(n) 
Average: O(n^2)
Worst Case: O(n^2)
"""


def bubble(unsorted: list) -> list:
    while True:
        swaps = 0
        for i in range(len(unsorted) - 1):
            current = unsorted[i]
            _next = unsorted[i + 1]
            if current > _next:
                temporary = current
                unsorted[i] = _next
                unsorted[i + 1] = temporary
                swaps += 1
        if swaps == 0:
            break
    return unsorted


if __name__ == "__main__":
    start = [5, 1, 4, 2, 8]
    print("Start array: ", start)
    print("Result: ", bubble(start))
