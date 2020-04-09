"""
Hash table
* key - value lookup
* collision & chaining
* Getting and setting a value from "good" hash table is O(1)
for "bad" hash table with lots of collisions is O(n)

"""


class HashMap():
    # array - storing data
    # hash function
    # collision handling
    def __init__(self):
        self.size = 6
        self.map = [None]*self.size

    def _get_hash(self, key):
        pass

    def add(self, key, value):
        pass

    def get(self, key):
        pass


