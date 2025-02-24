class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0 / values[i]))
        
        def bfs(query):
            x, y = query
            dq = deque([(x, 1.0)])
            visited = set()
            
            while dq:
                v = dq.popleft()
                if v in visited:
                    continue
                
                for adj in graph[v[0]]:
                    if adj[0] == y:
                        return adj[1] * v[1]
                    if adj[0] not in visited:
                        dq.append((adj[0], adj[1] * v[1]))
                visited.add(v[0])
            
            return -1.0
                

        res = []
        for x in queries:
            if x[0] not in graph or x[1] not in graph:
                res.append(-1.0)
                continue
            res.append(bfs(x))

        return res
