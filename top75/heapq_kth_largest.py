class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # res = []
        # def add(res, num):
        #     n = len(res)
        #     if n == 0:
        #         res.append(num)
        #         return res
        
        #     if num > res[0]:
        #         res = [num] + res
        #     elif num < res[-1]:
        #         res.append(num)
        #     else:
        #         m = n // 2
        #         while m >= 0 and m < n:
        #             if num <= res[m]:
        #                 if m + 1 >= n:
        #                     res.insert(m, num)
        #                     break
        #                 elif num >= res[m + 1]:
        #                     res.insert(m + 1, num)
        #                     break
        #                 else:
        #                     m = m + m // 2
        #             else:
        #                 m = m // 2
        #     return res

        # for x in nums:
        #     if len(res) < k:
        #         res = add(res, x)
        #     elif x >= res[-1]:
        #         res = add(res[:-1], x)
        # return res[-1]

        minheap = []
        for i in range(k):
            heapq.heappush(minheap, nums[i])
        for i in range(k, len(nums)):
            heapq.heappushpop(minheap, nums[i])
        return minheap[0]

        # pivot = nums[0]
        
        # left = [num for num in nums if num < pivot]
        # equal = [num for num in nums if num == pivot]
        # right = [num for num in nums if num > pivot]
        
        # if k <= len(right): return self.findKthLargest(right, k)
        # elif len(right) < k <= len(right) + len(equal): return equal[0]
        # else: return self.findKthLargest(left, k - len(right) - len(equal))