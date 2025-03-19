class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # tabulation
        dp = [0] + [-1] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c and dp[i - c] >= 0:
                    if dp[i] == -1:
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[-1]

        # # memoization
        # memo = {}
        # def recursion(amount, memo):
        #     if amount == 0:
        #         return 0
            
        #     if amount not in memo:
        #         memo[amount] = sys.maxsize
        #         for c in coins:
        #             if amount - c >= 0:
        #                 prev = recursion(amount - c, memo)
        #                 if prev >= 0:
        #                     memo[amount] = min(memo[amount], prev + 1)
            
        #     if memo[amount] == sys.maxsize:
        #         memo[amount] = -1
            
        #     return memo[amount]
        
        # res = recursion(amount, memo)
        # return res
