class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # m = 1
        # dp = [1] * n

        # def dfs(x, dp, m):
        #     for i in range(x + 1, len(dp)):
        #         if nums[x] < nums[i]:
        #             dp[x] = max(dp[x], dp[i] + 1)
        #             if dp[x] > m:
        #                 return dp[x]
        #     return m

        # for i in range(n - 2, -1, -1):
        #     m = dfs(i, dp, m)

        # return m

        res = []

        def binary_search(res, n):
            left = 0
            right = len(res) - 1

            while left <= right:
                mid = (left + right) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = binary_search(res, n)
                res[idx] = n
        
        return len(res)
