class MyCalendarThree:

#     def __init__(self):
#         self.arr = []

#     def book(self, start: int, end: int) -> int:
#         if start >= len(self.arr):
#             add = start - len(self.arr)
#             for _ in range(add):
#                 self.arr.append(0)
#         for i in range(start, end):
#             try:
#                 self.arr[i] += 1
#             except:
#                 self.arr.append(1)
#         return max(self.arr)
            
    
    def __init__(self):
        self.maxoverlaps= 1
        self.intervals =[]

    def book(self, start: int, end: int) -> int:
        self.intervals.append((start, +1 ))
        self.intervals.append((end, -1))
        
        self.intervals.sort()
        
        currmax=0
        for i in self.intervals:
            currmax+= i[1]
            self.maxoverlaps= max(self.maxoverlaps, currmax)

        return self.maxoverlaps


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)