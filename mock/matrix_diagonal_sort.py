class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        d = [(0, 0)]
        for x in range(1, m):
            d.append((x, 0))
        for y in range(1, n):
            d.append((0, y))
        
        for x, y in d:
            temp = []
            i, j = x, y
            while i < m and j < n:
                temp.append(mat[i][j])
                i += 1
                j += 1

            temp.sort()
            
            i, j = i - 1, j - 1
            while i >= 0 and j >= 0:
                mat[i][j] = temp.pop()
                i -= 1
                j -= 1
        
        return mat
            
        
