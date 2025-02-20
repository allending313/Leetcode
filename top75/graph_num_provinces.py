class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # notSeen = set(range(len(isConnected)))
        # res = []

        # def search(i):
        #     seen = set()
        #     curr = [i]
            
        #     while curr:
        #         x = curr.pop()
        #         for y in range(len(isConnected)):
        #             if isConnected[x][y] and y not in seen:
        #                 curr.append(y)
        #         seen.add(x)
        #     return seen

        # while notSeen:
        #     found = search(notSeen.pop())
        #     res.append(found)
        #     notSeen = notSeen.difference(found)

        # return len(res)

        seen = set()

        def dfs(x):
            for y in range(len(isConnected)):
                if isConnected[x][y] and y not in seen:
                    seen.add(y)
                    dfs(y)
        
        res = 0
    
        for i in range(len(isConnected)):
            if i not in seen:
                res += 1
                seen.add(i)
                dfs(i)
                
        return res