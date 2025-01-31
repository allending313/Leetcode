class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # x, y, res = [nums[0]], [nums[-1]], []

        # for i in range(1, len(nums) - 1):
        #     x.append(x[i - 1] * nums[i])
        # for i in range(1, len(nums) - 1):
        #     y.append(y[i - 1] * nums[-i - 1])

        # res = [a * b for a, b in zip([1] + x, y[::-1] + [1])]
        # return res

        l = len(nums)
        x, y = 1, 1
        res = [1] * l

        for i in range(l):
            res[i] *= x
            x *= nums[i]

            res[l-1-i] *= y
            y *= nums[l-1-i]
        return res
