"""
Sample use cases:
- word search engine
- word syntax checher/tips, where word is getting underlined if its not found in db
"""

class Trie:
    
    def __init__(self):
        head = {}

    def add(self, word):
        cur = self.head
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["*"] = True

    def search(self, word):
        cur = self.head

        for c in word:
            if not c in cur:
                return False
            cur = cur[c]
        if "*" in cur:
            return True
        return False
