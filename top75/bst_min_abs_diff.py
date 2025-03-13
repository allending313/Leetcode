# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.res = sys.maxsize
        self.prev = -sys.maxsize

        def inorder(self, root):
            if not root:
                return 
            
            inorder(self, root.left)
            self.res = min(self.res, root.val - self.prev)
            self.prev = root.val
            inorder(self, root.right)
        
        inorder(self, root)
        
        return self.res