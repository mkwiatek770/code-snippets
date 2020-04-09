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
        hash_value = sum([ord(char) for char in str(key)])
        return hash_value % self.size

    def add(self, key, value) -> bool:
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].apppend(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key) -> bool:
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        
        for index, pair in enumerate(self.map[key_hash]):
            if pair[0] == key:
                self.map[key_hash].pop(index)
                return True

    def __str__(self):
        print("---PHONEBOOK---")
        for item in self.map:
            if item is not None:
                print(item)

h = HashMap()
h.add('Bob', '500 272 111')
h.add('Helen', '123 123 421')
h.add('Helen', '123 444 444')
#str(h)
print(h.map)
h.delete('Bob')
print(h.map)
#str(h)

