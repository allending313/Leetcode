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
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.data:
                return False
            curr = curr.data[char]
        return True