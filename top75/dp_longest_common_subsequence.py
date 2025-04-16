class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m = len(s1)
        # n = len(s2)
        # memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # for row in range(1, m + 1):
        #     for col in range(1, n + 1):
        #         if s1[row - 1] == s2[col - 1]:
        #             memo[row][col] = 1 + memo[row - 1][col - 1]
        #         else:
        #             memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])

        # return memo[m][n]

        m, n = len(text1), len(text2)
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            pre = 0
            for j in range(1, n + 1):
                cur = dp[j]
                dp[j] = pre + 1 if text1[i-1] == text2[j-1] else max(dp[j-1], cur)
                pre = cur

        return dp[-1]