class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # r = defaultdict(int)
        # c = defaultdict(int)
        # res = 0

        # for i in range(len(grid)):
        #     row = []
        #     col = []
        #     for j in range(len(grid)):
        #         row.append(grid[i][j])
        #         col.append(grid[j][i])
        #     r[tuple(row)] += 1
        #     c[tuple(col)] += 1
        
        # for x in r.keys():
        #     if x in c:
        #         res += r[x] * c[x]

        # return res

        d = defaultdict(int)
        res = 0

        for x in grid:
            d[tuple(x)] += 1
        
        for y in zip(*grid):
            res += d[tuple(y)]
        
        return res