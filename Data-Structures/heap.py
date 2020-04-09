"""
Tree-based data structure.
Max heap - the highest element is on top
Min heap - the lowest element is on top

 A heap is used as a queue where the min (or max if max heap) is always accessed in O(1) time.  If the min (which is always at index 0 is popped off, then the next smallest takes its place.     Remember its stored linearly yet indexed logarithmically.  Therefore its a "priority" queue. 
"""

class MinIntHeap:

    capacity: int = 10
    size: int = 0
    items: list = []

    def _get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def _get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def _get_parent_index(self, child_index: int) -> int:
        return (child_index - 2) / 2
    
    def has_left_child(self, index: int) -> bool:
        return self._get_left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        return self._right_left_child_index(index) < self.size

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
        if (self.size == self.capacity):
            self.items = self.items[:] * 2
            self.capacity *= 2


    def peek(self):
        try:
            return self.items[0]
        except IndexError:
            print("There has to be at least one element")
    
    def poll(self):
        item = self.items[0]
        self.items[0] = self.items[size - 1]
        this.size -= 1
        self.heapify_down()
        return item
    
    def add(self, item):
        ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while (self.has_left_child(index)):
            smaller_child_index = self.get_left_child_index(index)
            if (self.has_right_child(index) and self.right_child(index) < self.left_child(index)):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] > self.items[smaller_child_index]:
                self.swap(index, smaller_child_index)
            else:
                break
            index = smaller_child_index

