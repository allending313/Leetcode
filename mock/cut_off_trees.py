class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        res = 0

        pq = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(pq, (forest[i][j], i, j))

        coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(target, sx, sy):
            stack = deque([(sx, sy, 0)])
            seen = set()
            seen.add((sx, sy))

            while stack:
                curr = stack.popleft()
                if forest[curr[0]][curr[1]] == target[0]:
                    return curr[2]
                for x, y in coord:
                    i, j = x + curr[0], y + curr[1]
                    if i < 0 or i >= m or j < 0 or j >= n:
                        continue
                    if (i, j) in seen or forest[i][j] == 0:
                        continue
                    seen.add((i, j))
                    stack.append((i, j, curr[2] + 1))
            return -1

        sx, sy = 0, 0
        while pq:
            target = heapq.heappop(pq)
            steps = bfs(target, sx, sy)
            if steps == -1:
                return -1
            res += steps
            sx, sy = target[1], target[2]

        return res

