class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph = defaultdict(list)
        # for x, y, t in times:
        #     graph[x].append((y, t))
        
        # seen = [-1] * n
        # seen[k - 1] = 0
        
        # stack = [k]
        
        # while stack:
        #     neighbors = []
        #     for node in stack:
        #         for y, t in graph[node]:
        #             if seen[y - 1] == -1 or seen[node - 1] + t < seen[y - 1]:
        #                 seen[y - 1] = seen[node - 1] + t
        #                 neighbors.append(y)
        #     stack = neighbors
                
        # if any(x == -1 for x in seen):
        #     return -1
        
        # return max(seen)
                    
        graph = defaultdict(list)
        for x, y, t in times:
            graph[x].append((y, t))
        
        seen = {}
        stack = [(0, k)]

        while stack:
            t, node = heapq.heappop(stack)
            if node in seen:
                continue

            seen[node] = t

            for y, w in graph[node]:
                if y not in seen:
                    heapq.heappush(stack, (t + w, y))
        
        if len(seen) != n:
            return -1
        return max(seen.values())