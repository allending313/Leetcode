class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         def diagonalIterate(val, x, y):
#             try:
#                 cur = matrix[y][x]
#             except:
#                 return True
#             if cur == val:
#                 return diagonalIterate(cur, x+1, y+1)
#             else:
#                 return False
        
#         for x in range(len(matrix[0])):
#             if not diagonalIterate(matrix[0][x], x, 0):
#                 return False
#         for y in range(1,len(matrix)):
#             if not diagonalIterate(matrix[y][0], 0, y):
#                 return False
#         return True

    def isToeplitzMatrix(self, m):
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(m[:-1], m[1:]))