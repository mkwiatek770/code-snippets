"""
LIFO - Last In First Out
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return False

        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            print("There are no elements!")
            return
        print(self.top.data)


s = Stack()
s.push(6)
s.push(8)
assert s.top.data == 8
assert s.top.next.data == 6
assert s.pop() == 8
assert s.top.data == 6
assert s.top.next is None
    
