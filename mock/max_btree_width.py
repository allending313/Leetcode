# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root, 0]])
        res = 0

        while q:
            res = max(res, q[-1][1] - q[0][1])

            for _ in range(len(q)):
                [node, i] = q.popleft()
                if node.left:
                    q.append([node.left, i * 2])
                if node.right:
                    q.append([node.right, i * 2 + 1])
        
        return res + 1