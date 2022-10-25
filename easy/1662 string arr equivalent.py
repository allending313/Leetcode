import functools

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return functools.reduce(lambda x, y: x + y, word1) == functools.reduce(lambda x, y: x + y, word2)