class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # edge = defaultdict(list)
        # t = grid[0][0]
        # n = len(grid)
        # coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # edge[t].append((0, 0))
        
        # def dfs(x, y):
        #     if grid[x][y] < 0:
        #         return
        #     grid[x][y] = -1
            
        #     for i, j in coord:
        #         if x + i < 0 or x + i >= n or y + j < 0 or y + j >= n:
        #             continue
        #         if grid[x + i][y + j] <= t:
        #             dfs(x + i, y + j)
        #         else:
        #             edge[grid[x + i][y + j]].append((x + i, y + j))
        
        # while edge:
        #     keylist = [key for key in edge.keys() if key <= t]
        #     for key in keylist:
        #         if key > t:
        #             continue
        #         for x, y in edge[key]:
        #             dfs(x, y)
        #         edge.pop(key, [])
        #     if grid[n - 1][n - 1] == -1:
        #         return t
        #     t += 1
            
        n = len(grid)
        seen = set([(0, 0)])
        edge = [(grid[0][0], 0, 0)]
        coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while edge:
            t, x, y = heapq.heappop(edge)
            if x == n - 1 and y == n - 1:
                return t
            
            for i, j in coord:
                if x + i < 0 or x + i >= n or y + j < 0 or y + j >= n or (x + i, y + j) in seen:
                    continue
                seen.add((x + i, y + j))
                heapq.heappush(edge, (max(t, grid[x + i][y + j]), x + i, y + j))