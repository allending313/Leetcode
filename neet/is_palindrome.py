class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

        # q = []
        # for x in s:
        #     if x.isalpha():
        #         q.append(x.lower())
        #     if x.isdigit():
        #         q.append(x)
        # if q[:len(q)//2] == q[len(q)-1:(len(q)-1)//2:-1]:
        #     return True
        # return False
