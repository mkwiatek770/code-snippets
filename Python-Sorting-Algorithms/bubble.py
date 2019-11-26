"""
Bubble Sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

Second Pass:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )
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
    print("Start list: ", start)
    print("Result: ", bubble(start))
