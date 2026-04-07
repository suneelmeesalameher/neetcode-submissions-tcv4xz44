class TrieNode:

    def __init__(self):
        self.children={}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for w in word:
            if w not in current.children:
                current.children[w]=TrieNode()
            current=current.children[w]
        current.endOfWord=True



    def search(self, word: str) -> bool:
        current = self.root

        for w in word:
            if w not in current.children:
                return False
                #curreent.children[w]=TrieNode()
            current=current.children[w]
        if current.endOfWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for w in prefix:
            if w not in current.children:
                return False
                #curreent.children[w]=TrieNode()
            current=current.children[w]
        return True
        