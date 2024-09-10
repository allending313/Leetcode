class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x, y = 0, len(nums) - 1
        
        while x <= y:
            m = x + ((y - x) // 2)

            if nums[m] == target:
                return m
            if nums[m] > target:
                y = m - 1
            if nums[m] < target:
                x = m + 1

        return - 1