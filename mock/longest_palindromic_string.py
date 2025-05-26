class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # def isValid(s):
        #     return s == s[::-1]

        # d = defaultdict(list)
        # for i, c in enumerate(s):
        #     d[c].append(i)
        
        # res = ""

        # for i, c in enumerate(s):
        #     for j in d[c]:
        #         if j < i or j - i < len(res):
        #             continue
        #         if isValid(s[i:j + 1]):
        #             res = s[i:j + 1]
        
        # return res

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)



        # inutition: two types of palindromes: even and odd
        # iterate twice through the string to check both cases
        # if the current substring is a palindrome, see if we can expand

        def expand(s, start, end):
            res = (0, 0)
            while start >= 0 and end < len(s) and s[start] == s[end]:
                res = (start, end)
                start -= 1
                end += 1
    
            return res

        start, end = 0, 0

        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i + 1)
            
            if odd[1] - odd[0] > end - start:
                start, end = odd

            if even[1] - even[0] > end - start:
                start, end = even
            
        
        return s[start:end + 1]
        

        