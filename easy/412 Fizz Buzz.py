"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
"""

class Solution:
    def fizzBuzz(n: int):
        answer = [None] * n
        for i in range(0,n):
            if (i+1)%3 == 0:
                if (i+1)%5 == 0:
                    answer[i] = "FizzBuzz"
                else:
                    answer[i] = "Fizz"
            elif (i+1)%5 == 0:
                if (i+1)%3 == 0:
                    answer[i] = "FizzBuzz"
                else:
                    answer[i] = "Buzz"
            else:
                answer[i] = str(i+1)
        return answer

    #def fizzBuzz(self, n):
        #return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]