# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # x, y = 1, n
        # while x <= y:
        #     m = (x + y) // 2
        #     if (g := guess(m)) == 0:
        #         return m
        #     elif g == 1:
        #         x = m + 1
        #     else:
        #         y = m - 1

        # return -1

        x, y = 1, n
        g = (x + y) >> 1
        while (res := guess(g)) != 0:
            if res == 1:
                x = g + 1
            else:
                y = g - 1
            g = (x + y) >> 1

        return g