class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = collections.defaultdict(int)
        for x in s: count[x] += 1
        for x in t: count[x] -= 1
        return not any(count.values())
        
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT

        # return sorted(t) == sorted(s)