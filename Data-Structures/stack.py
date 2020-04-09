"""
LIFO - Last In First Out
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return False

        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            print("There are no elements!")
            return
        print(self.head.data)


s = Stack()
s.push(6)
s.push(8)
assert s.head.data == 8
assert s.head.next.data == 6
assert s.pop() == 8
assert s.head.data == 6
assert s.head.next is None
    
