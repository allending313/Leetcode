class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x, y = 0, len(nums) - 1
            
        while x <= y:
            m = x + ((y - x) // 2)
            
            if nums[m] == target:
                return m
           
            if target < nums[m]:
                if target <= nums[y] and nums[m] > nums[y]:
                    x = m + 1
                else:
                    y = m - 1
            if target > nums[m]:
                if target >= nums[x] and nums[m] < nums[x]:
                    y = m - 1
                else:
                    x = m + 1
            
        return -1