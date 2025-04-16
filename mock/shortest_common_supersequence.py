class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if str1[row - 1] == str2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        i, j = m, n
        res = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif memo[i - 1][j] > memo[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1
        
        res = ''.join(res[::-1])
        return str1[:i] + str2[:j] + res