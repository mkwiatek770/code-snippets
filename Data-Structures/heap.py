"""
Tree-based data structure.
Max heap - the highest element is on top
Min heap - the lowest element is on top

 A heap is used as a queue where the min (or max if max heap) is always accessed in O(1) time.  If the min (which is always at index 0 is popped off, then the next smallest takes its place.     Remember its stored linearly yet indexed logarithmically.  Therefore its a "priority" queue. 

Insert O(logn)
Get min/max (depends what kind of Heap) in O(1)

Indexes operations:
parent index = (i-1)/2
left child = 2*i + 1
right child = 2*i + 2

"""
from abc import ABC, abstractmethod
from typing import Union


class BinaryHeap(ABC):

    def __init__(self):
        self.items = []

    @abstractmethod
    def push(self, value: int) -> None:
        """Add element into heap."""
        pass

    @abstractmethod
    def pop(self, value: int) -> bool:
        """Push value from heap."""
        pass

    @abstractmethod
    def _heapify_up(self):
        pass

    @abstractmethod
    def _heapify_down(self):
        pass

    def swap(self, i: int, j: int) -> None:
        """Swap elements in heap."""
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def _get_parent_index(self, index):
        if index == 0:
            return None
        return (index-1) // 2

    def _get_left_child_index(self, index):
        left_index = 2*index + 1
        if left_index >= len(self.items):
            return None
        return left_index

    def _get_right_child_index(self, index):
        right_index = 2*index + 2
        if right_index >= len(self.items):
            return None
        return right_index

    def _get_parent(self, index) -> Union[int, None]:
        """Get parent of child with given index."""
        try:
            return self.items[self._get_parent_index(index)]
        except TypeError:
            return None

    def _get_left_child(self, index) -> Union[int, None]:
        """Get left child of parent by given index."""
        try:
            return self.items[self._get_left_child_index(index)]
        except TypeError:
            return None

    def _get_right_child(self, index) -> Union[int, None]:
        """Get right child of parent by given index."""
        try:
            return self.items[self._get_right_child_index(index)]
        except TypeError:
            return None


class MinIntHeap:

    def __init__(self):
        self.capacity: int = 10
        self.items: list = []

    def _get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def _get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def _get_parent_index(self, child_index: int) -> int:
        return (child_index - 2) // 2

    def has_left_child(self, index: int) -> bool:
        return self._get_left_child_index(index) < len(self.items)

    def has_right_child(self, index: int) -> bool:
        return self._get_right_child_index(index) < len(self.items)

    def has_parent(self, index: int) -> bool:
        return self._get_parent_index(index) >= 0

    def left_child(self, index: int) -> int:
        return self.items[self._get_left_child_index(index)]

    def right_child(self, index: int) -> int:
        return self.items[self._get_right_child_index(index)]

    def parent(self, index: int) -> int:
        return self.items[self._get_parent_index(index)]

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def ensure_extra_capacity(self):
        if len(self.items) == self.capacity:
            self.items = self.items[:] * 2
            self.capacity *= 2

    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print("There has to be at least one element")

    def poll(self):
        item = self.items[0]
        self.items[0] = self.items[len(self.items) - 1]
        self.heapify_down()
        return item

    def add(self, item):
        # self.ensure_extra_capacity()
        self.items.append(item)
        self.heapify_up()

    def heapify_up(self):
        index = len(self.items) - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self._get_parent_index(index), index)
            index = self._get_parent_index(index)

    def heapify_down(self):
        index = 0
        while (self.has_left_child(index)):
            smaller_child_index = self._get_left_child_index(index)
            if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
                smaller_child_index = self._get_right_child_index(index)

            if self.items[index] > self.items[smaller_child_index]:
                self.swap(index, smaller_child_index)
            else:
                break
            index = smaller_child_index


class MaxIntHeap(BinaryHeap):
    """Implementation of max heap."""

    def max(self) -> Union[int, None]:
        """Get maximum value of heap."""
        if len(self.items) >= 1:
            return self.items[0]
        print("Heap is empty")

    def push(self, value: int) -> None:
        """Append element into heap."""
        self.items.append(value)
        self._heapify_up()

    def pop(self, value: int) -> bool:
        """Pop element from heap."""
        pass

    def _heapify_up(self):
        index = len(self.items) - 1
        while _has_parent(index):
            value = self.items[index]
            parent_index = self._get_parent(index)
            if value <= self.items[parent_index]:
                break
            self.swap(value, parent_index)

    def _heapify_down(self):
        pass


def test_heap_max


h = MaxIntHeap()
h.push(6)
assert h.max() == 6

# h = MinIntHeap()
# h.add(15)
# h.add(6)
# h.add(7)
# print(h.items)
# assert h.items[0] == 6
# assert h.items[1] == 7
# assert h.poll() == 6
