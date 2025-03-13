# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        s = [root]
        res = []

        while s:
            avg = 0
            low = []
            for x in s:
                avg += x.val
                if x.left:
                    low.append(x.left)
                if x.right:
                    low.append(x.right)
            res.append(round(avg / len(s), 5))
            s = low

        return res
