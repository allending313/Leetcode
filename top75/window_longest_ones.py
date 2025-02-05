class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        x, y = 0, 0
        m = c = 0

        while y < len(nums):
            c += nums[y]
            y += 1
            if (c + k) >= (y - x):
                m = max(m, y - x)
            else:
                c -= nums[x]
                x += 1
        
        return m
