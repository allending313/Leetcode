class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, hq = 0, 0, []

        for b, a in sorted(list(zip(nums2, nums1)), reverse=True):
            prefixSum += a
            heappush(hq, a)
            if len(hq) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(hq)
        
        return res