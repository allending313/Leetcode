class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # d = defaultdict(set)
        # r = defaultdict(set)
        # s = set()
        # self.res = 0

        # for x in connections:
        #     d[x[0]].add(x[1])
        #     r[x[1]].add(x[0])
        
        # def dfs(root):
        #     if root in s:
        #         return
        #     s.add(root)
        #     if root in d:
        #         for x in d.pop(root):
        #             if x not in s:
        #                 self.res += 1
        #                 dfs(x)
        #     if root in r:
        #         for x in r.pop(root):
        #             dfs(x)

        # dfs(0)
        # return self.res

        # d = defaultdict(set)
        # for x, y in connections:
        #     d[x].add((y, True))
        #     d[y].add((x, False))
        
        # q = deque([(0, False)])
        # s = set()
        # res = 0

        # while q:
        #     root, add = q.popleft()
        #     s.add(root)

        #     if add:
        #         res += 1
            
        #     for adj in d[root]:
        #         if adj[0] not in s:
        #             q.append(adj)
        
        # return res

        d = defaultdict(list)
        for x, y in connections:
            d[x].append((y, 1))
            d[y].append((x, 0))
        
        def dfs(root, prev):
            res = 0
            for adj, add in d[root]:
                if adj != prev:
                    res += add + dfs(adj, root)
            return res

        return dfs(0, -1)
        