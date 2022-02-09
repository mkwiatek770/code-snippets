"""
Example from "Python Cookbook 3rd edition 1.5"

Heap queue is a special tree structure in which each parent node is less than or equal to its child node.
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    @property
    def is_empty(self):
        return len(self._queue) == 0


class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Task('foo'), 1)
    q.push(Task('bar'), 5)
    q.push(Task('spam'), 4)
    q.push(Task('grok'), 1)

    # do tasks in priority order
    while not q.is_empty:
        print('Doing:', q.pop())
