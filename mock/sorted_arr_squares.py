class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # use two pointers to iterate through the nums list with
        # # the right pointer starting at the lowest positive number and moving right
        # # the left pointer starting at the lowest negative number and moving left
        # # at each iteration: check which pointer has a smaller abs()
        # # and append the square of that number to the results arr
        # n = len(nums)
        # if nums[0] >= 0 or n == 1:
        #     return [x * x for x in nums]
        # if nums[-1] < 0:
        #     return [x * x for x in nums][::-1]

        # x, y = 0, 1
        # while y < n:
        #     if nums[x] < 0 and nums[y] >= 0:
        #         break
        #     x += 1
        #     y += 1

        # res = []
        # while x >= 0 or y < n:
        #     left = sys.maxsize if x < 0 else abs(nums[x])
        #     right = sys.maxsize if y >= n else abs(nums[y])
            
        #     if left < right:
        #         res.append(nums[x] ** 2)
        #         x -= 1
        #     elif left > right:
        #         res.append(nums[y] ** 2)
        #         y += 1
        #     else:
        #         res.append(nums[x] ** 2)
        #         x -= 1
        #         res.append(nums[y] ** 2)
        #         y += 1
        
        # return res

        n = len(nums)
        x, y = 0, n - 1
        res = deque()

        while x <= y:
            if abs(nums[x]) > abs(nums[y]):
                res.appendleft(nums[x] ** 2)
                x += 1
            else:
                res.appendleft(nums[y] ** 2)
                y -= 1
        
        return list(res)
        
