class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
#         res = []
#         for i in range(len(nums) - 2):
#             list = nums[i+1:]
#             first = nums[i]
#             for j in range(len(list) - 1):
#                 second = list[j]
#                 final = list[j+1:]
#                 for third in final:
#                     res.append(first+second+third)
                    
#         res.append(target)
#         res.sort()
#         index = res.index(target)
#         lower, upper = None, None
#         if index == 0:
#             return res[1]
#         if index == len(res) - 1:
#             return res[index-1]
#         else:
#             lower = res[index-1]
#             upper = res[index+1]
#             if abs(lower - target) > abs(upper - target):
#                 return upper
#             else: 
#                 return lower
            
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans