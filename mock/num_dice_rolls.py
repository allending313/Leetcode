class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(n, target):
            res = 0
            if target > n * k:
                return 0
            if target < n:
                return 0
            
            if n == 1:
                if target <= k:
                    return 1
                else:
                    return 0
    
            for i in range(1, k + 1):
                if target - i >= 0:
                    res += dfs(n - 1, target - i)
                
            return res
        
        return dfs(n, target) % (10 ** 9 + 7)
            