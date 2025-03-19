# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.curr = 0
    #     self.res = []
    #     self.__dfs(root)
    
    # def __dfs(self, node):
    #     if not node:
    #         return
    #     self.__dfs(node.left)
    #     self.res.append(node.val)
    #     self.__dfs(node.right)

    # def next(self) -> int:
    #     self.curr += 1
    #     return self.res[self.curr - 1]

    # def hasNext(self) -> bool:
    #     return self.curr < len(self.res)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()