class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            res += n % 2
            res = res << 1
            n = n >> 1
        
        return res >> 1

        