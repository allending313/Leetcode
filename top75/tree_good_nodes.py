# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # self.res = 0
        # def dfs(self, root, m):
        #     if root and root.val >= m:
        #         self.res += 1
        #         m = root.val
        #     if root.left:
        #         dfs(self, root.left, m)
        #     if root.right:
        #         dfs(self, root.right, m)
        
        # dfs(self, root, -sys.maxsize)
        # return self.res

        def dfs(root, m):
            if not root:
                return 0
            if root.val >= m:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, m) + dfs(root.right, m)
        
        return dfs(root, root.val)
