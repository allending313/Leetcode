class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def getSlice(nums, index):
            res = [-sys.maxsize, nums[index], -sys.maxsize]
            if index > 0:
                res[0] = nums[index - 1]
            if index < len(nums) - 1:
                res[2] = nums[index + 1]
            return res
    
        x, y = 0, len(nums) - 1
        while x <= y:
            m = (x + y) // 2
            s = getSlice(nums, m)
            if s[1] < s[0]:
                y = m - 1
            elif s[1] < s[2]:
                x = m + 1
            else:
                return m
        return -1


            
            