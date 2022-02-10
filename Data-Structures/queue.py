"""
FIFO - First In First Out
"""
from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self) -> bool:
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def add(self, data):
        node = Node(data)
        
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        if self.is_empty():
            return False

        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


# custom deque
class DoubleEndedQueue(deque):

    def __lshift__(self, value):
        self.append(value)
    
    def __rshift__(self, value):
        self.appendleft(value)


q = Queue()
q.add(14)
q.add(6)
assert q.head.data == 14
assert q.tail.data == 6
q.remove()
assert q.head.data == 6
assert q.tail.data == 6
q.remove()
assert q.head == None

