class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """res = []
        t_list = list(t)
        
        def window(index: int) -> str:
            check = t_list.copy()
            out = ""
            while index < len(s):
                out += s[index]
                if s[index] in check:
                    check.remove(s[index])
                index += 1
                if not check:
                    return out
            return ""
        
        for i, char in enumerate(s):
            if char in t_list:
                if w := window(i):
                    res.append(w)
        
        res = sorted(res, key=len)
        print(res)
        return res[0] if res else ""
        """
        
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1):          #index j from 1
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]
            