# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
        
#         def astrix(s, p):
#             # print("astrix", s, p)
#             if not p:
#                 return True
#             if not s and p[0] != '*':
#                 return False
            
#             if p[0] == '*':
#                 return astrix(s, p[1:])
            
#             if p[-1] == '?':
#                 if s[-1].isalpha():
#                     return astrix(s[:-1], p[:-1])
#                 return False
            
#             if p[-1].isalpha():
#                 if s[-1] == p[-1]:
#                     return astrix(s[:-1], p[:-1])
#                 return False
            
#             if p[0] == '?':
#                 for i, c in enumerate(s):
#                     if c.isalpha():
#                         if helper(s[i + 1:], p[1:]):
#                             return True
#             elif p[0].isalpha():
#                 for i, c in enumerate(s):
#                     if c == p[0]:
#                         if helper(s[i + 1:], p[1:]):
#                             return True            
#             return False
        
#         def helper(s, p):
#             # print("helper", s, p)
#             if not s and not p:
#                 return True
            
#             if s and not p:
#                 return False
            
            
#             if p[0] == '?':
#                 if s and s[0].isalpha():
#                     return helper(s[1:], p[1:])
#                 return False
            
#             if p[0] != '*':
#                 if s and s[0] == p[0]:
#                     return helper(s[1:], p[1:])
#                 return False

#             if p[-1] == '?':
#                 if s and s[-1].isalpha():
#                     return helper(s[:-1], p[:-1])
#                 return False
            
#             if p[-1] != '*':
#                 if s and s[-1] == p[-1]:
#                     return helper(s[:-1], p[:-1])
#                 return False
            
#             return astrix(s, p[1:])
        
#         return helper(s, p)  
               
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
    
        last_match = 0
        star = -1
    
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                last_match = i
                star = j
                j += 1
            elif star != -1:
                print(i, j, star, last_match)
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False
    
        while j < len(p) and p[j] == '*':
            j += 1
    
        return j == len(p)
    
            