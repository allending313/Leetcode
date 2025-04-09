# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(x, y):
            if y < x:
                return None
            
            m = (x + y) // 2
            node = TreeNode(nums[m])
            node.left = helper(x, m - 1)
            node.right = helper(m + 1, y)
            
            return node
        
        return helper(0, len(nums) - 1)