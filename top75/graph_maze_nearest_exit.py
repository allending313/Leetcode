class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dq = deque([(entrance, 0)])

        while dq:
            v = dq.popleft()
            x, y = v[0]

            if maze[x][y] == '+':
                continue
            
            if x == 0 or x == m - 1 or y == 0 or y == n -1:
                if v[0] != entrance:
                    return v[1]
            
            #up
            if x > 0 and maze[x - 1][y] == '.':
                dq.append(([x - 1, y], v[1] + 1))
            #down
            if x < m - 1 and maze[x + 1][y] == '.':
                dq.append(([x + 1, y], v[1] + 1))
            #right
            if y < n - 1 and maze[x][y + 1] == '.':
                dq.append(([x, y + 1], v[1] + 1))
            #left
            if y > 0 and maze[x][y - 1] == '.':
                dq.append(([x, y - 1], v[1] + 1))
            
            maze[x][y] = '+'

        return -1