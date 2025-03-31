class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        neighbors = [[] for _ in range(n)]
        for v1, v2 in connections:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        minDist = [n] * n
        res = []
        
        def dfs(node, parent, dist):
            if minDist[node] == n:
                minDist[node] = dist
                for neighbor in neighbors[node]:
                    if neighbor != parent:
                        actual = dfs(neighbor, node, dist + 1) 
                        if actual >= dist + 1:
                            res.append([node, neighbor])
                        minDist[node] = min(minDist[node], actual)
            return minDist[node]

        dfs(0, -1, 0)
        return res
                            
                            