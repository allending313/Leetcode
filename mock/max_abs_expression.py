class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        f = [[0] * len(arr1) for _ in range(4)]
        for i in range(len(arr1)):
            f[0][i] = i + arr1[i] + arr2[i]
            f[1][i] = i + arr1[i] - arr2[i]
            f[2][i] = i - arr1[i] + arr2[i]
            f[3][i] = i - arr1[i] - arr2[i]
        
        res = 0
        for i in range(4):
            res = max(res, max(f[i]) - min(f[i]))
        
        return res