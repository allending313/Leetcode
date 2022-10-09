# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """ naive O(n^2) solution
        stack = []
        def traverse(root):
            if root:
                stack.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
                
        traverse(root)
        for i in range(len(stack)):
            if (k-stack[i]) in (stack[:i] + stack[i+1:]):
                return True
            
        return False
        """
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False