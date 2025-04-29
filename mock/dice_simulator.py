class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @lru_cache(None)
        def backtrack(n, last, times):
            if n == 0:
                return 1
            
            res = 0
            for i in range(6):
                if i == last:
                    if times < rollMax[i]:
                        res += backtrack(n - 1, i, times + 1)
                else:
                    res += backtrack(n - 1, i, 1)
            return res % (10**9 + 7)
        
        return backtrack(n, -1, 0)