# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, n):
            if not node:
                return 0

            n = n * 10 + node.val

            if not (node.right or node.left):
                return n

            return dfs(node.right, n) + dfs(node.left, n)
        
        return dfs(root, 0)