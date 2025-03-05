class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a + b + c > 0:
            cbit, bbit, abit = c % 2, b % 2, a % 2
            
            if not cbit:
                if abit & bbit:
                    res += 2
                elif abit | bbit:
                    res += 1
            elif not (abit | bbit):
                res += 1

            a, b, c = a >> 1, b >> 1, c >> 1
        
        return res
