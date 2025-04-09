class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        seenM = set()
        seenN = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    seenM.add(i)
                    seenN.add(j)
                    matrix[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if i in seenM or j in seenN:
                    matrix[i][j] = 0

        
        