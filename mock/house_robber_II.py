class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        def robHouse(nums):
            p1, p0 = 0, 0
            for x in nums:
                p0, p1 = max(p1 + x, p0), p0
            
            return max(p0, p1)
        
        return max(robHouse(nums[0:-1]), robHouse(nums[1:]))