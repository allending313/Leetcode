class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for x in s:
            if x in d:
                stack.append(x)
            elif len(stack) == 0 or d[stack.pop()] != x:
                return False
        return len(stack) == 0
        
        # stack = []
        
        # for x in s:
        #     if ord(x) in [40, 91, 123]:
        #         stack.append(x)
        #         continue
        #     if len(stack) > 0 and (diff := ord(x) - ord(stack[-1])) > 0 and diff < 3:
        #         stack.pop()
        #         continue
        #     return False
        
        # return len(stack) == 0
                 