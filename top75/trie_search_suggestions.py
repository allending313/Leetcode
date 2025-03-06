class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        t.transform(sorted(products))
        return t.autocomplete(searchWord)

class Trie:
    def __init__(self):
        self.data = {}
        self.words = []
        self.end = False
    
    def transform(self, l: List[str]) -> None:
        for x in l:
            curr = self
            for char in x:
                if char not in curr.data:
                    curr.data[char] = Trie()
                curr = curr.data[char]
                if len(curr.words) < 3:
                    curr.words.append(x)
            curr.end = True
    
    def autocomplete(self, word: str) -> List[List[str]]:
        res = []
        curr = self
        for char in word:
            if char not in curr.data:
                curr = Trie()
                res.append([])
                continue
            curr = curr.data[char]
            res.append(curr.words)
        return res

