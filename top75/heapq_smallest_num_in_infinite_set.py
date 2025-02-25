class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.hq = []
        self.seen = set()
        

    def popSmallest(self) -> int:
        if len(self.hq) == 0:
            self.curr += 1
            return self.curr - 1
        res = heapq.heappop(self.hq)
        self.seen.remove(res)
        return res
        

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.seen:
            heapq.heappush(self.hq, num)
            self.seen.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)