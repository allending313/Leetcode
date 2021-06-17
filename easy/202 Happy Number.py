"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(n: int) -> bool:
        
        def sds(n):
            n = str(n)
            digits = list(n)
            sum = 0
            for x in digits:
                sum += (int(x))**2
            return sum

        counter = 0
        while True:
            sum = sds(n)
            n = sum
            if sum == 1:
                return True
            counter += 1
            if counter > 100:
                return False
            
    print(isHappy(19))

        
"""
def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1
"""

    