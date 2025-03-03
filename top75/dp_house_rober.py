class Solution:
    def rob(self, nums: List[int]) -> int:
        # p3, p2, p1 = 0, 0, 0

        # for x in nums:
        #     p0 = x + max(p3, p2)
        #     p3, p2, p1 = p2, p1, p0

        # return max(p2, p1)

        prev_prev, prev = 0, 0
        for x in nums:
            prev, prev_prev = max(prev_prev + x, prev), prev
            
        return prev