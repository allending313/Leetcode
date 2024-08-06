class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0

        for x in s:
            if (x-1) not in s:
                c = 1
                while (x+c) in s:
                    c += 1
                l = max(c, l)
        return l