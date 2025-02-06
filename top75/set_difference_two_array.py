class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)

        # res = [[], []]
        
        # for x in s1:
        #     if x not in s2:
        #         res[0].append(x)
        
        # for x in s2:
        #     if x not in s1:
        #         res[1].append(x)

        for x in nums1:
            if x in s2:
                s1.discard(x)
                s2.remove(x)
        
        return [list(s1), list(s2)]