class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, low = 0, prices[0]

        for x in prices:
            low = min(low, x)
            m = max(m, x - low)

        return m