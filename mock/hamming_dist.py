class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        new = x ^ y
        while new > 0:
            new = new & (new-1)
            res += 1
        return res