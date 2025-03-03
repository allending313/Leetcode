class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = []

        # for x in cost[::-1]:
        #     if len(dp) < 2:
        #         dp.append(x)
        #         continue
        #     if dp[-1] < dp[-2]:
        #         dp.append(x + dp[-1])
        #     else:
        #         dp.append(x + dp[-2])

        # return min(dp[-1], dp[-2])
        
        prev, prev_prev = cost[1], cost[0]
        
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev, prev_prev)
            prev_prev = prev
            prev = curr
        
        return min(prev, prev_prev)