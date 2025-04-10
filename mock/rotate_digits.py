class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        
        good = set([2, 5, 6, 9])
        bad = set([3, 4, 7])
        
        for x in range(1, n + 1):
            found = False
            while x:
                d = x % 10
                if d in bad:
                    found = False
                    break
                if d in good:
                    found = True
                x = x // 10
            
            if found:
                res += 1
        
        return res
        