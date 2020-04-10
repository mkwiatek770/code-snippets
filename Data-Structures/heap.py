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
    def insert(self, value: int) -> None:
        """Add element into heap."""
        pass

    @abstractmethod
    def delete(self) -> int:
        """Delete head from heap."""
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

    def _has_parent(self, index: int) -> bool:
        if index == 0:
            return False
        return True

    def _has_left_child(self, index: int) -> bool:
        return self._get_left_child_index(index) is not None

    def _has_right_child(self, index: int) -> bool:
        return self._get_right_child_index(index) is not None

    def _get_parent_index(self, index: int) -> int:
        if index == 0:
            return None
        return (index-1) // 2

    def _get_left_child_index(self, index: int) -> int:
        left_index = 2*index + 1
        if left_index >= len(self.items):
            return None
        return left_index

    def _get_right_child_index(self, index: int) -> int:
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


class MinIntHeap(BinaryHeap):
    """Implementation of min heap."""

    @property
    def min(self) -> Union[int, None]:
        if len(self.items) >= 1:
            return self.items[0]
        print("Heap is empty")

    def insert(self, value: int) -> None:
        self.items.append(value)
        self._heapify_up()

    def delete(self) -> int:
        pass

    def _heapify_up(self) -> None:
        index = len(self.items) - 1
        while self._has_parent(index):
            value = self.items[index]
            parent_index = self._get_parent_index(index)
            if value >= self.items[parent_index]:
                break
            self.swap(index, parent_index)
            index = parent_index

    def _heapify_down(self) -> None:
        pass


class MaxIntHeap(BinaryHeap):
    """Implementation of max heap."""

    @property
    def max(self) -> Union[int, None]:
        """Get maximum value of heap."""
        if len(self.items) >= 1:
            return self.items[0]
        print("Heap is empty")

    def insert(self, value: int) -> None:
        self.items.append(value)
        self._heapify_up()

    def delete(self) -> int:
        self.swap(0, len(self.items) - 1)
        value = self.items.pop(len(self.items) - 1)
        self._heapify_down()
        return value

    def _heapify_up(self):
        index = len(self.items) - 1
        while self._has_parent(index):
            value = self.items[index]
            parent_index = self._get_parent_index(index)
            if value <= self.items[parent_index]:
                break
            self.swap(index, parent_index)
            index = parent_index

    def _heapify_down(self):
        index = 0
        while self._has_left_child(index):
            bigger_child_index = self._get_left_child_index(index)
            if self._has_right_child(index) and self._get_right_child(index) > self._get_left_child(index):
                bigger_child_index = self._get_right_child_index(index)

            if self.items[index] > self.items[bigger_child_index]:
                break
            self.swap(index, bigger_child_index)
            index = bigger_child_index


def test_heap_min():
    heap = MinIntHeap()
    heap.insert(15)
    assert heap.min == 15
    heap.insert(17)
    assert heap.min == 15
    heap.insert(4)
    assert heap.min == 4
    assert heap.items == [4, 17, 15]
    heap.insert(16)
    assert heap.items == [4, 16, 15, 17]
    assert heap.delete() == 4
    assert heap.items == [15, 16, 17]


def test_heap_max():
    heap = MaxIntHeap()
    heap.insert(16)
    assert heap.max == 16
    heap.insert(5)
    assert heap.max == 16
    heap.insert(17)
    assert heap.max == 17
    assert heap.items == [17, 5, 16]
    heap.insert(14)
    assert heap.items == [17, 14, 16, 5]
    heap.insert(17)
    print(heap.items)
    assert heap.items == [17, 17, 16, 5, 14]

    assert heap.delete() == 17
    assert heap.items == [17, 14, 16, 5]
    heap.delete()
    assert heap.items == [16, 14, 5]


if __name__ == "__main__":
    test_heap_max()
    test_heap_min()
