"""
Linked is is a list where each element has a pointer to next element.
First element is called head. Last is called tail.

Advantages
- insert and delete can be quick, O(1) prepend and O(n) for append
Disadvantages
- slow to get nth element O(n)
"""


class Node:
    
    def __init__(self, data):
        self.next = None
        self.data = data



class LinkedList:

    def __init__(self, head=None):
        if head:
            self.head = head
        else:
            self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(value)

    def prepend(self, value):
        old_head = self.head

        self.head = Node(value)
        self.head.next = old_head

    def delete_with_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next != None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False


node = Node(1)
linked = LinkedList(node)
linked.append(5)
linked.append(6)
assert linked.head.next.next.data == 6
linked.delete_with_value(5)
assert linked.head.next.data == 6
linked.prepend(7)
assert linked.head.data == 7
assert linked.head.next.data == 1
