class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res = 1
        rep = [1]
        count = defaultdict(int)
        
        count[text[0]] += 1
        for i in range(1, len(text)):
            count[text[i]] += 1
            if text[i] == text[i - 1]:
                rep.append(rep[-1] + 1)
            else:
                rep.append(1)
        
        i = len(text) - 1
        while i >= 0:
            curr = rep[i]
            if i - curr - 1 >= 0 and text[i - curr - 1] == text[i]:
                curr += rep[i - curr - 1]
            
            if count[text[i]] > curr:
                curr += 1
            
            res = max(res, curr)
            i -= rep[i]
        
        return res