# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        prev = None
        carry = 0
        
        while l1 or l2 or carry:
            node = ListNode(carry)
            carry = 0
            
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            
            if node.val > 9:
                carry = 1
                node.val = node.val % 10
            
            if not res:
                res = node
            else:
                prev.next = node
            prev = node
        
        return res