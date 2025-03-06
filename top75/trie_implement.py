class Trie:

    def __init__(self):
        self.data = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.data:
                curr.data[char] = Trie()
            curr = curr.data[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.data:
                return False
            curr = curr.data[char]
        
        if curr.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.data:
                return False
            curr = curr.data[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)