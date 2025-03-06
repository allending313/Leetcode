class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort()
        # prev = [-sys.maxsize, sys.maxsize]
        # res = len(points) + 1

        # for x in points:
        #     print(res, prev, x)
        #     if (x[0] >= prev[0] and x[0] <= prev[1]) or x[1] <= prev[1]:
        #         prev = [max(x[0], prev[0]), min(x[1], prev[1])]
        #         res -= 1
        #     else:
        #         prev = x
        
        # return res

        points.sort(key = lambda x: x[1])
        prev = points[0][1]
        res = 1

        for x in points[1:]:
            if prev < x[0]:
                res += 1
                prev = x[1]
        
        return res