class Solution:
    # def findMin(self, s):        
    #     # x, y are the outer chars
    #     x, y = s[0], s[-1]
    #     n = len(s)

    #     i, j = 1, n - 2

    #     while i < n:
    #         if s[i] == y:
    #             break
    #         i += 1
        
    #     while j >= 0:
    #         if s[j] == x:
    #             break
    #         j -= 1

    #     if i < n - 1 - j:
    #         return (True, i)
    #     else:
    #         return (False, j)

    # def minMovesToMakePalindrome(self, s: str) -> int:
    #     # try to match the outer characters so that we can
    #     # delete them and recursively progress
    #     # find the min number of moves it takes to match outer chars

    #     # base case: only one char is by default a valid palindrome
    #     n = len(s)
    #     if n < 2:
    #         return 0

    #     # case: outer already matching
    #     if s[0] == s[-1]:
    #         return self.minMovesToMakePalindrome(s[1:-1])
        
    #     # case: need to find min swaps
    #     (left, minSwaps) = self.findMin(s)
    #     if left:
    #         s = s[minSwaps] + s[:minSwaps] + s[minSwaps + 1:]
    #         return minSwaps + self.minMovesToMakePalindrome(s[1:-1])
    #     elif not left:
    #         s = s[:minSwaps] + s[minSwaps + 1:] + s[minSwaps]
    #         return n - 1 - minSwaps + self.minMovesToMakePalindrome(s[1:-1])
    #     else:
    #         print(minSwaps, s)

    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0 
        while len(s) > 2: 
            lo = s.find(s[-1])
            hi = s.rfind(s[0])
            if lo < len(s)-hi-1: 
                ans += lo 
                s = s[:lo] + s[lo+1:-1]
            else: 
                ans += len(s)-hi-1
                s = s[1:hi] + s[hi+1:]
        return ans
