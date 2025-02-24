class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # rot = set()
        # m, n = len(grid), len(grid[0])
        # self.fresh = 0
        # time = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             rot.add((i, j))
        #         elif grid[i][j] == 1:
        #             self.fresh += 1
        
        # def spread(rotten):
        #     rotting = set()
        #     for i, j in rotten:
        #         if grid[i][j] == 1:
        #             grid[i][j] = 2
        #             self.fresh -= 1
        #             if (i, j) in rotting:
        #                 rotting.remove((i, j))
        #         if i > 0 and grid[i - 1][j] == 1:
        #             rotting.add((i - 1, j))
        #         if i < m - 1 and grid[i + 1][j] == 1:
        #             rotting.add((i + 1, j))
        #         if j > 0 and grid[i][j - 1] == 1:
        #             rotting.add((i, j - 1))
        #         if j < n - 1 and grid[i][j + 1] == 1:
        #             rotting.add((i, j + 1))
    
        #     return rotting

        # rot = spread(rot)
        # while rot:
        #     rot = spread(rot)
        #     time += 1
        
        # return -1 if self.fresh > 0 else time

        rot = set()
        m, n = len(grid), len(grid[0])
        fresh = 0
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while rot and fresh > 0:
            rotting = set()
            for i, j in rot:
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh -= 1
                    rotting.add((i - 1, j))
                if i < m - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh -= 1
                    rotting.add((i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh -= 1
                    rotting.add((i, j - 1))
                if j < n - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh -= 1
                    rotting.add((i, j + 1))
            rot = rotting
            time += 1
        
        return -1 if fresh > 0 else time