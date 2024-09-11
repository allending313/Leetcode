class Solution:
    def findMin(self, nums: List[int]) -> int:
        x, y = 0, len(nums) - 1
        if nums[x] <= nums[y]:
            return nums[x]
            
        while x < y:
            m = x + ((y - x) // 2)

            if nums[m] < nums[y]:
                y = m
            else:
                x = m + 1
        return nums[x]

