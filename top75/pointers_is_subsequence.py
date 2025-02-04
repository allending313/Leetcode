class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x, y = 0, 0
        while x < len(s) and y < len(t):
            if s[x] == t[y]:
                x += 1
            y += 1
        
        return x == len(s)

# # DP approach
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         nxt = [{} for _ in range(len(t) + 1)]
#         for i in range(len(t) - 1, -1, -1):
#             nxt[i] = nxt[i + 1].copy()
#             nxt[i][t[i]] = i + 1
        
#         print(nxt)

#         i = 0
#         for c in s:
#             if c in nxt[i]:
#                 i = nxt[i][c]
#             else:
#                 return False
#         return True