# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # def dfs(node):
        #     if not node:
        #         return None
            
        #     hasOne = False
            
        #     if not dfs(node.right):
        #         node.right = None
        #     else:
        #         hasOne = True
                
        #     if not dfs(node.left):
        #         node.left = None
        #     else:
        #         hasOne = True
            
        #     if node.val == 1:
        #         return True
        #     return hasOne
        
        # if dfs(root):
        #     return root
        # else:
        #     return None
        
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val == 0:
            return None
        return root