class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        x, y = 1, max(piles)
        
        while x <= y:
            m = (x + y) // 2

            hours = 0
            for p in piles:
                hours += ceil(p / m)

            if hours <= h:
                y = m - 1
            else:
                x = m + 1
        
        return x