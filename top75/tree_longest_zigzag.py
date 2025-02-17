# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root, left, right):
            self.res = max(self.res, left, right)

            if root.left:
                dfs(root.left, right + 1, 0)
            if root.right:
                dfs(root.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.res