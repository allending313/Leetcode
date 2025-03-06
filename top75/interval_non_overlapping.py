class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # prev = -sys.maxsize
        # res = 0

        # for interval in intervals:
        #     x, y = interval
        #     if x < prev:
        #         if y < prev:
        #             prev = y   
        #         res += 1
        #     else:
        #         prev = y
        
        # return res

        intervals.sort(key = lambda x: x[1])
        prev = -sys.maxsize
        res = 0

        for x in intervals:
            if x[0] < prev:
                res += 1
            else:
                prev = x[1]
        
        return res