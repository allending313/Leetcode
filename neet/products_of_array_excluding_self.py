class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre, suf = 1, 1
        res = [1] * l

        for i in range(l):
            res[i] *= pre
            pre *= nums[i]

            res[l-1-i] *= suf
            suf = suf*nums[l-1-i]
        return res
        
        # pre, suf = [1], [1]
        # for i in range(0, len(nums)-1):
        #     pre.append(nums[i] * pre[i])

        # for i in range(0, len(nums)-1):
        #     suf.append(nums[-i-1] * suf[-1])

        # return [x * y for x, y in zip(pre, reversed(suf))]
