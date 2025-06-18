# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = head
        prev = None

        # within a while loop: check for matching val
        # case (no match) => go next
        # case (match) => update prev.next

        while head:
            if head.val == val:
                if prev:
                    prev.next = head.next
                else:
                    newHead = head.next
            else:
                prev = head
            
            head = head.next
        
        return newHead