class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # x, y, s = 0, k, 0

        # for i in range(y):
        #     s += nums[i]
        # m = s

        # while y < len(nums):
        #     s += nums[y] - nums[x]
        #     m = max(m, s)
        #     x += 1
        #     y += 1
        
        # return m / k

        w = sum(nums[:k])
        m = w

        for i in range(len(nums) - k):
            w += nums[i + k] - nums[i]
            m = max(m, w)
        
        return m / k