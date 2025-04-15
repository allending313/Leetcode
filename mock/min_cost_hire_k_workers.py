class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # [(wage/quality ratio, wage, quality)]
        ratio = []
        for x, y in zip(quality, wage):
            ratio.append((y / x, y, x))
        
        ratio.sort()
        res = sys.maxsize
        tq = 0
        heap = []

        for r, w, q in ratio:
            heapq.heappush(heap, - q)
            tq += q

            if len(heap) > k:
                tq += heapq.heappop(heap)
            
            if len(heap) == k:
                res = min(res, tq * r)
        
        return res
            