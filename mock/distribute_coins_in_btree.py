# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        # def dfs(node, parent) -> int:
        #     if not node:
        #         return 0

        #     moves = dfs(node.left, node) + dfs(node.right, node)
        #     need = node.val - 1

        #     if parent:
        #         parent.val += need

        #     moves += abs(need)

        #     return moves

        # return dfs(root, None) 

        def dfs(node):
            if not node:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            moves = left[0] + right[0]
            need = node.val - 1 + left[1] + right[1]

            moves += abs(need)
            return moves, need
        
        return dfs(root)[0]
