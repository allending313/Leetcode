class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        hq = []
        n = len(costs)
        x, y = candidates, n - candidates - 1

        if x > y:
            for cost in costs:
                heappush(hq, (cost, 0))
        else:
            for i in range(candidates):
                heappush(hq, (costs[i], i))
            for i in range(n - candidates, n):
                heappush(hq, (costs[i], i))

        for i in range(k):
            cost, index = heappop(hq)
            res += cost

            if x <= y:
                if index <= x:
                    heappush(hq, (costs[x], x))
                    x += 1
                else:
                    heappush(hq, (costs[y], y))
                    y -= 1
        return res
                
