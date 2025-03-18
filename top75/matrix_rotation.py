class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for i, x in enumerate(list(zip(*matrix[::-1]))):
        #     matrix[i] = x
    
        n = len(matrix)
        for row in range((n + 1) // 2):
            for col in range(n // 2):
                print(row, col)
                (
                    matrix[row][col],
                    matrix[~col][row],
                    matrix[~row][~col],
                    matrix[col][~row],
                ) = (
                    matrix[~col][row],
                    matrix[~row][~col],
                    matrix[col][~row],
                    matrix[row][col],
                )
        