class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        # # keep track of edges
        # edge = [[] for _ in range(n)]
        # res = [0] * n
        
        # # initialize edge list
        # for x, y in paths:
        #     edge[x - 1].append(y)
        #     edge[y - 1].append(x)
        
        # def dfs(garden):
        #     garden -= 1
        #     if res[garden] != 0:
        #         return
            
        #     possible = [1,2,3,4]
        #     for neighbor in edge[garden]:
        #         if res[neighbor - 1] != 0:
        #             possible[res[neighbor - 1] - 1] = 0
            
        #     for x in possible:
        #         if x != 0:
        #             res[garden] = x
        #             break
            
        #     for neighbor in edge[garden]:
        #         dfs(neighbor)
        
        # for i in range(1, n + 1):
        #     dfs(i)
        
        # return res

        edge = defaultdict(list)
        res = [0] * n

        for x, y in paths:
            edge[x].append(y)
            edge[y].append(x)
        
        for i in range(1, n + 1):
            flowers = {1, 2, 3, 4}
            for neighbor in edge[i]:
                if res[neighbor - 1] in flowers:
                    flowers.remove(res[neighbor - 1])
            res[i - 1] = flowers.pop()
        
        return res
        
            