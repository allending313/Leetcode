class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        Q, v = deque([(0, 0, 0, k)]), set()
        
        if k >= m + n - 2: return m + n - 2
        
        while Q:
            steps, x, y, k = Q.popleft()
            if (x, y) == (m - 1, n - 1): return steps
            
            for dx, dy in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):
                if 0 <= dx < m and 0 <= dy < n and k - grid[dx][dy] >= 0:
                    new = (dx, dy, k - grid[dx][dy])
                    if new not in v:
                        v.add(new)
                        Q.append((steps + 1,) + new)
            
        return -1