class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
                
            for i, x in enumerate(nums):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(x)
                backtrack(path, used)
                path.pop()
                used[i] = False
                
        backtrack([], [False] * len(nums))
                
        return res