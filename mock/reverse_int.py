class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        negate = False
        if x < 0:
            negate = True
            x *= -1
            
        while x:
            res *= 10
            res += x % 10
            x = x // 10
        
        if negate:
            res *= -1
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            res = 0
    
        return res