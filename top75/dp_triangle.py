class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # res = [[0] * (i + 1) for i in range(len(triangle))]
        # res[0][0] = triangle[0][0]

        # for i in range(1, len(triangle)):
        #     for j in range(i + 1):
        #         if j > 0 and j < i:
        #             res[i][j] = triangle[i][j] + min(res[i - 1][j - 1], res[i - 1][j])
        #         elif j == 0:
        #             res[i][j] = triangle[i][j] + res[i - 1][j]
        #         else:
        #             res[i][j] = triangle[i][j] + res[i - 1][j - 1]
        
        # return min(res[-1])

        prev = triangle[0]
        res = []

        for i in range(len(triangle) - 1):
            for j in range(i + 1):
                if not res:
                    res.append(prev[j] + triangle[i + 1][j])
                else:
                    res[-1] = min(res[-1], prev[j] + triangle[i + 1][j])
                res.append(prev[j] + triangle[i + 1][j + 1])

            prev = res
            res = []

        return min(prev)