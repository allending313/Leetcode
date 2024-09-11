class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0]) - 1
        height = len(matrix) - 1

        x, y = 0, height
        
        while x <= y:
            m = x + ((y - x) // 2)
            if matrix[m][0] > target:
                y = m - 1
            if matrix[m][0] < target:
                if m < height and matrix[m + 1][0] > target:
                    break
                x = m + 1
            if matrix[m][0] == target:
                return True
        
        row = m
        x, y = 0, width

        while x <= y:
            m = x + ((y - x) // 2)

            if matrix[row][m] > target:
                y = m - 1
            if matrix[row][m] < target:
                x = m + 1
            if matrix[row][m] == target:
                return True
        
        return False

        