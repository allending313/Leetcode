# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def r(node):
            if not node:
                return None
            
            if not node.next:
                return node
            
            second = node.next
            temp = second.next
            second.next = node
            node.next = r(temp)
            
            return second
        
        return r(head)
            