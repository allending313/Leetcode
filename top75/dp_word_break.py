class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if dp[i - len(word)] and s[:i].endswith(word):
                    dp[i] = True
                    break
        
        return dp[-1]