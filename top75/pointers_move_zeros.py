class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # x, y = 0, len(nums) - 1
        
        # while x < y:
        #     if nums[x] == 0:
        #         del nums[x]
        #         nums.insert(y, 0)
        #         y -= 1
        #     else:
        #         x += 1
    
        x = 0
        for y in range(len(nums)):
            if nums[y] != 0:
                nums[y], nums[x] = nums[x], nums[y]
                x += 1
        
        