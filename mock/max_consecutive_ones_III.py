class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     flip = 0
        #     j = i
        #     curr = 0
        #     while j < len(nums):
        #         if nums[j] == 0:
        #             flip += 1
        #             if flip > k:
        #                 break
        #         curr += 1
        #         j += 1
            
        #     if curr > res:
        #         res = curr
        
        # return res

        # list of length k to store flipped indicies
        # flip = deque()
        # x, y = 0, 0
        # res = 0

        # while y < len(nums):
        #     if nums[y] == 0:
        #         flip.append(y)
                
        #         # check for length of flip to maintain size to k
        #         if len(flip) > k:
        #             x = flip.popleft() + 1
            
        #     res = max(res, y - x + 1)
        #     y += 1
        
        # return res

        x, y = 0, 0
        flip = 0

        while y < len(nums):
            if nums[y] == 0:
                flip += 1
            if flip > k:
                if nums[x] == 0:
                    flip -= 1
                x += 1
            y += 1
        
        return y - x