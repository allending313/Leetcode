class Solution:
    def search(self, nums: List[int], target: int) -> bool:     
        
        ##########################################
        # Either right or left side will be sorted
        ##########################################

        x, y = 0, len(nums) - 1
        while x <= y:
            m = (x + y) // 2
            
            if nums[m] == target:
                return True
            
            if nums[m] == nums[y]:
                y -= 1                
            elif nums[x] <= nums[m]:
                if target < nums[m] and target >= nums[x]:
                    y = m - 1
                else:
                    x = m + 1
            else:
                if target <= nums[y] and target > nums[m]:
                    x = m + 1
                else:
                    y = m - 1
        
        return False