class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        words = s.split(' ')
        for word in words:
            res += word[::-1]
            res += " "
        
        return res[:-1]