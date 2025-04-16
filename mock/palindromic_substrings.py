class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # intuition: num of palindromic substrings in a valid palindrom
        # is equal to it's length // 2
        n = len(s)
        res = 0

        for i in range(n):
            # odd case:
            x, y = i, i
            while x >= 0 and y < n and s[x] == s[y]:
                x -= 1
                y += 1
            res += (y - x) // 2

            # even case:
            x, y = i, i + 1
            while x >= 0 and y < n and s[x] == s[y]:
                x -= 1
                y += 1
            res += (y - x) // 2
        
        return res