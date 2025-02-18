# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # res = []

        # def bfs(root, level):
        #     if not root:
        #         return
        #     if len(res) <= level:
        #         res.append(0)
            
        #     res[level] = res[level] + root.val

        #     bfs(root.left, level + 1)
        #     bfs(root.right, level + 1)
        
        # bfs(root, 0)

        # return max(enumerate(res), key = lambda x: x[1])[0] + 1

        d = defaultdict(int)

        def bfs(root, level):
            if not root:
                return
            d[level] += root.val

            bfs(root.left, level + 1)
            bfs(root.right, level + 1)
        
        bfs(root, 1)
        
        return max(d, key = d.get)