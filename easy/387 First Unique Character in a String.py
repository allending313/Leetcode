"""
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(s: str) -> int:
        dict = {}.fromkeys(list(s), 0)
        for x in s:
            dict[x] += 1
        unique = {k: v for (k,v) in dict.items() if v == 1}
        if len(unique) == 0:
            return -1
        target = next(iter(unique))
        for count, x in enumerate(s):
            if x == target:
                return count



    print(firstUniqChar("aabb"))