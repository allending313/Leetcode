# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # def dfs(root, prev):
        #     if not root:
        #         return 0

        #     prev = prev + [root.val]
        #     s = 0
        #     c = 0
            
        #     for x in prev[::-1]:
        #         s += x
        #         if s == targetSum:
        #             c += 1
            
        #     return c + dfs(root.left, prev) + dfs(root.right, prev)
        
        # return dfs(root, [])
                
        def dfs(root, dic, prefixSum):
            if not root:
                return 0
            
            prefixSum += root.val
            count = dic[prefixSum - targetSum]
            dic[prefixSum] += 1

            count += dfs(root.left, dic, prefixSum) + dfs(root.right, dic, prefixSum)
            dic[prefixSum] -= 1

            return count
        
        return dfs(root, defaultdict(int, {0: 1}), 0)