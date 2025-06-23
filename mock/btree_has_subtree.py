# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMatch(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val == node2.val:
            return self.isMatch(node1.left, node2.left) and self.isMatch(node1.right, node2.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return
            if self.isMatch(node, subRoot):
                return True
            return helper(node.left) or helper(node.right)
        
        return helper(root) or False