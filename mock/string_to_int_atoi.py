class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        res = 0
        negate = False
        
        if len(s) > 0:
            if s[0] == '-':
                negate = True
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
        
        num = 0
        for c in s:
            if not c.isdigit():
                break
                
            num *= 10
            num += int(c)
        
        if num > 2 ** 31 - 1:
            num =  2 ** 31 - 1
            if negate:
                num += 1
        
        if negate:
            return -num
        
        return num