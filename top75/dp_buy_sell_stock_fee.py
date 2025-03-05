class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dont, have = 0, 0

        for i in range(1, len(prices)):
            growth = prices[i] - prices[i - 1]
            dont = max(dont, have + growth - fee)
            have = max(dont, have + growth)

        return dont

