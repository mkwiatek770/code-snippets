


class Node:

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: int):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def contains(self, value: int) -> bool:
        if self.data == value:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)



class BinaryTree:

    def __init__(self, head=None):
        if head:
            self.head = head
        else:
            self.head = None

    def create_node(self, value: int) -> Node:
        if self.head is None:
            self.head = Node(value)
        else:
            self.head.insert(value)
            
    def has_value(self, value) -> bool:
        if self.head is None:
            return False
        return self.head.contains(value)





n1 = Node(10)
tree = BinaryTree(n1)
tree.create_node(5)
tree.create_node(15)
tree.create_node(8)


print(tree.head.left.data)
print(tree.head.right.data)
print(tree.head.left.right.data)
print(tree.has_value(4))
print(tree.has_value(8))
print(tree.has_value(15))

