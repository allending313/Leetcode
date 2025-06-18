# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        s = [root]
        depth = 1

        while s:
            nextLevel = []
            for node in s:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                if not node.left and not node.right:
                    return depth
            s = nextLevel
            depth += 1
        
        return depth
