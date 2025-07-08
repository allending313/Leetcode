# Given a collection of numbers, nums, that might contain duplicates
# return all possible unique permutations in any order.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res = set()

        # def backtrack(path, used):
        #     if len(path) == len(nums):
        #         res.add(tuple(path[:]))
        #         return
            
        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
        #         path.append(nums[i])
        #         used[i] = True
        #         backtrack(path, used)
        #         used[i] = False
        #         path.pop()
        
        # backtrack([], [False for _ in range(len(nums))])

        # return list(res)

        res = []
        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    backtrack(path + [key])
                    counter[key] += 1
        
        backtrack([])
        return res