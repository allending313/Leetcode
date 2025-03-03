class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 1, 2]
        p3, p2, p1 = 1, 1, 2

        for _ in range(2, n):
            p0 = 2 * p1 + p3
            p3, p2, p1 = p2, p1, p0
        
        if n < 3:
            return n

        return p1 % (10 ** 9 + 7)
