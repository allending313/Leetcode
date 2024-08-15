class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = [-1] * 128
        res, left = 0, 0
        for right, c in enumerate(s):
            if prev[ord(c)] >= left:
                left = prev[ord(c)] + 1
            prev[ord(c)] = right
            res = max(res, right - left + 1)
            
        return res
        
        # w = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in w:
        #         w.remove(s[l])
        #         l += 1
        #     w.add(s[r])
        #     res = max(res, r - l + 1)
        # return res