class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dont = 0

        for i in range(1, len(prices)):
            dont = max(dont, dont + prices[i] - prices[i - 1])
        
        return dont