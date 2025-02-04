class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # d = defaultdict(list)
        # res = 0
        # for i, x in enumerate(nums):
        #     if x in d:
        #         d[x].pop()
        #         if d[x] == []:
        #             d.pop(x)
        #         res += 1
        #     else:
        #         d[k - x].append(i)
        
        # return res

        nums.sort()
        x, y, res = 0, len(nums) - 1, 0

        while x < y:
            if (s := nums[x] + nums[y]) == k:
                res += 1
                x += 1
                y -= 1
            elif s > k:
                y -= 1
            else:
                x += 1

        return res
                    