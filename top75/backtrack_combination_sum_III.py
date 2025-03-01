class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(curr, low, t):
            if len(curr) == k:
                if t == 0:
                    res.append(curr)
                return
            
            for i in range(low + 1, 10):
                if i > t:  
                    return
                backtrack(curr + [i], i, t - i)
        
        backtrack([], 0, n)
        return res