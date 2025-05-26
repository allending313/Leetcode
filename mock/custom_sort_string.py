class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        
        for c in order:
            d[c] = 0
        
        junk = ""
        res = ""
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                junk += c
        
        for k, v in d.items():
            res += k * v
        
        return res + junk