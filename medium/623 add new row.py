# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            res = TreeNode(val=val, left=root)
            return res
        nodeList = [root]
        while depth > 2:
            newList = []
            for node in nodeList:
                if node.left:
                    newList.append(node.left)
                if node.right:
                    newList.append(node.right)
            depth -= 1
            nodeList = newList
        for node in nodeList:
            l = TreeNode(val, node.left, None)
            r = TreeNode(val, None, node.right)
            node.left = l
            node.right = r
        return root

        """ DFS SOLUTION
        def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root or d <= 0 : return None
        if d == 1:
            return TreeNode(v, root, None)
        if d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            root.left == self.addOneRow(root.left, v, d - 1)
            root.right == self.addOneRow(root.right, v, d - 1)
        return root
        """