class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # utilize a minHeap to store and ordered list of points where lower distance to the origin will be at the top of the heap
        # minHeap = []
        
        # # iterate through the list of points to push them with their respecitve distance to the origin onto the minheap
        # for x, y in points:
        #     distance = math.sqrt((x * x) + (y * y))
        #     heapq.heappush(minHeap, (distance, x, y))
        
        # # pop the k smallest distances from the minheap and append their points to the resulting list
        # res = []
        # for _ in range(k):
        #     _, x, y = heapq.heappop(minHeap)
        #     res.append([x, y])
        
        # return res

        minHeap = []

        for x, y in points:
            distance = -math.sqrt((x * x) + (y * y))
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (distance, x, y))
            else:
                heapq.heappush(minHeap, (distance, x, y))
            
        return [(x, y) for _, x, y in minHeap]

