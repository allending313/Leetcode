class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        counter = 1
        while self.s and price >= self.s[-1][0]:
            _, c = self.s.pop()
            counter += c
        self.s.append((price, counter))
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)