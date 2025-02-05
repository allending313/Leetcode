# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         x, y = 0, 0
#         m = c = 0

#         while y < len(nums):
#             c += nums[y]
#             y += 1
#             if (c + 1) >= (y - x):
#                 m = max(m, y - x)
#             else:
#                 c -= nums[x]
#                 x += 1
        
#         return m - 1

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = p = c = 0

        for x in nums:
            if x:
                c += 1
                m = max(m, p + c)
            else:
                p, c = c, 0

        return m - (m == len(nums))