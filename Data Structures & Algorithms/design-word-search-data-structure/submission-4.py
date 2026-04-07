class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root

        for w in word:
            if w not in current.children:
                current.children[w]=TrieNode()
            current=current.children[w]
        current.endOfWord=True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            current = root
            for i in range(j,len(word)):
                if word[i]!='.':
                    if word[i] not in current.children:
                        return False
                    current=current.children[word[i]]
                else:
                    children=list(current.children.values())
                    for child in children:
                        if dfs(i+1,child):
                            return True
                    return False
            if current.endOfWord:
                return True
            else:
                return False
        return dfs(0,self.root)