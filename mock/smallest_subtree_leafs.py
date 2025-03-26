# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dic = defaultdict(set)
        # level = []
        
        # def bfs(node, dic, level, h):
        #     if not node:
        #         return set()
            
        #     if len(level) <= h:
        #         level.append([])
            
        #     if not node.right and not node.left:
        #         dic[node.val] = {node.val}
        #         level[h].append(node.val)
        #         return {node.val}
            
        #     children = bfs(node.right, dic, level, h + 1) | bfs(node.left, dic, level, h + 1)
        #     dic[node.val] = dic[node.val] | ({node.val} | children)
            
        #     return dic[node.val]
        
        # bfs(root, dic, level, 0)
        
        # curr = root
        
        # leaf = set(level[-1])
        
        # while curr:
        #     if curr.right and leaf == leaf & dic[curr.right.val]:
        #         curr = curr.right
        #     elif curr.left and leaf == leaf & dic[curr.left.val]:
        #         curr = curr.left
        #     else:
        #         break
        
        # return curr

        @lru_cache(None)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        curr = root
        while curr:
            l, r = height(curr.left), height(curr.right)

            if l == r:
                return curr
            elif l > r:
                curr = curr.left
            else:
                curr = curr.right
        
        return curr
            
        
        
            