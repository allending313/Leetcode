class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = sys.maxsize
        
        while q:
            x, y = q.popleft()
            for c in coord:
                i = x + c[0]
                j = y + c[1]
                
                if i >= 0 and i < m and j >= 0 and j < n:
                    if mat[i][j] > mat[x][y] + 1:
                        mat[i][j] = mat[x][y] + 1
                        q.append((i, j))
                
        return mat
        
            