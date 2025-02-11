class RecentCounter:

    # def __init__(self):
    #     self.q = []

    # def ping(self, t: int) -> int:
    #     while self.q:
    #         if self.q[0] < t - 3000:
    #             self.q.pop(0)
    #         else:
    #             break
        
    #     self.q.append(t)
    #     return len(self.q)

    def __init__(self):
        self.q = []
        self.s = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[self.s] < t - 3000:
            self.s += 1
        return len(self.q) - self.s


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)