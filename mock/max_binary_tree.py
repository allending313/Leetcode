# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(nums):
            if not nums:
                return None

            max_idx = nums.index(max(nums))
            node = TreeNode(nums[max_idx])
            
            if max_idx != 0:
                node.left = tree(nums[:max_idx])

            if max_idx + 1 < len(nums):
                node.right = tree(nums[max_idx + 1:])

            return node
        
        return tree(nums)
