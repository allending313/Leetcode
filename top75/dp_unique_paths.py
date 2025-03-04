class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        
        return grid[-1][-1]

        # combinatorics solution
        # return math.factorial(n + m - 2) // (math.factorial(n - 1) * math.factorial(m - 1))