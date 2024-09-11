class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k: int) -> bool:
            time = h
            for x in piles:
                time -= math.ceil(x / k)
                if time < 0:
                    return False
            return True

        x, y = 1, max(piles)
        res = y

        while x <= y:
            m = (x + y) // 2
            if possible(m):
                y = m - 1
                res = m
            else:
                x = m + 1
        return res
