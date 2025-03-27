# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        q = [root]
        foundx, foundy = None, None
        
        while q:
            if foundx and foundy:
                return foundx != foundy
            elif foundx or foundy:
                return False
            
            nxt = []
            for node in q:
                if node.left:
                    nxt.append(node.left)
                    if node.left.val == x:
                        foundx = node
                    if node.left.val == y:
                        foundy = node
                    
                if node.right:
                    nxt.append(node.right)
                    if node.right.val == x:
                        foundx = node
                    if node.right.val == y:
                        foundy = node
            q = nxt
        return 
    