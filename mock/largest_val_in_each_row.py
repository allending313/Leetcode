# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # if not root:
        #     return res
        # s = [root]
        # m = -sys.maxsize
        
        # while s:
        #     n = []
        #     for x in s:
        #         if x.val > m:
        #             m = x.val
        #         if x.left:
        #             n.append(x.left)
        #         if x.right:
        #             n.append(x.right)
        #     s = n
        #     res.append(m)
        #     m = -sys.maxsize
        
        # return res

        arr=[]
        def preOrder(Node, level):
            if not Node: return
            if len(arr)<=level: arr.append(-2**31)
            arr[level]=max(arr[level], Node.val)

            preOrder(Node.left, level+1)
            preOrder(Node.right, level+1)
        
        preOrder(root, 0)
        return arr
        