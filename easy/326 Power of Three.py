"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""
def isPowerOfThree(n):
    # if n <= 0:
    #         return False
    #     return (3 ** 19) % n == 0

    if n == 1:
        return True

    temp = divThree(n)
    if temp == 1:
        return True
    elif temp == 0:
        return False
    else:
        return isPowerOfThree(temp)
    

def divThree(num):
    if num%3 == 0:
        return num/3
    else:
        return 0

print(isPowerOfThree(27))