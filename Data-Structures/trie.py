"""
Sample use cases:
- word search engine
- word syntax checher/tips, where word is getting underlined if its not found in db
"""

class Node:
    
    def __init__(self, children=None, is_complete_word=None):
        if children:
            self.children = list(children)
        else:
            self.children = []
        self.is_complete_word = is_complete_word

