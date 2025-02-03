class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # # minLeft < x < maxRight
        # x = [sys.maxsize]
        # y = [-sys.maxsize]

        # for i in range(len(nums) - 1, 0, -1):
        #     if (m := nums[i]) > y[0]:
        #         y = [m] + y
        #     else:
        #         y = [y[0]] + y
        
        # for i in range(0, len(nums) - 1):
        #     if x[-1] < nums[i] and nums[i] < y[i]:
        #         return True
            
        #     if (m := nums[i]) < x[-1]:
        #         x = x + [m]
        #     else:
        #         x = x + [x[-1]]
            
        # return False

        min_arr = [sys.maxsize] * len(nums)
        max_arr = [-sys.maxsize] * len(nums)

        min_arr[0] = nums[0]
        max_arr[-1] = nums[-1]

        for i in range(1, len(nums)):
            if (min_arr[i-1] < nums[i]):
                min_arr[i] = min_arr[i-1]
            else:
                min_arr[i] =  nums[i]

        for i in range(len(nums) - 2, -1, -1):
            if (max_arr[i+1] > nums[i]):
                max_arr[i] = max_arr[i+1]
            else:
                max_arr[i] =  nums[i]

        for i in range(1, len(nums) - 1):
            if min_arr[i] < nums[i] < max_arr[i]:
                return True

        return False