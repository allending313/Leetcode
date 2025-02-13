# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # def recursive(root, h) -> int:
        #     if not root:
        #         return h
        #     else:
        #         return max(recursive(root.right, h + 1), recursive(root.left, h + 1))

        # return recursive(root, 0)

        stack = [(root, 1)]
        res = 0
        while stack and stack[0][0]:
            (node, h) = stack.pop()
            res = max(res, h)

            if node.left:
                stack.append((node.left, h + 1))
            if node.right:
                stack.append((node.right, h + 1))
            
        return res
            