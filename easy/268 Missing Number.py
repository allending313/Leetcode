"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

class Solution:
    def missingNumber(nums):
        nums.sort()
        start = 0
        end = len(nums) - 1
        if nums[start] != start:
            return start
        elif nums[end] != end + 1:
            return end + 1
        while (end - start) > 1:
            mid = start + (end - start)//2
            if nums[mid] > mid:
                end = mid
            elif nums[mid] == mid:
                start = mid
        return start + 1

    print(missingNumber([0,1,2,3,5,6]))