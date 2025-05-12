class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, i, s):
            if s == target:
                res.append(path[:])
                return
            if s > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            backtrack(path, i, s + candidates[i])
            path.pop()
            backtrack(path, i + 1, s)
        
        backtrack([], 0, 0)
        return res