# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        curr = head
        even = head.next
        temp = head.next
        
        while curr.next and temp.next:
            curr.next = curr.next.next
            temp.next = temp.next.next

            curr = curr.next
            temp = temp.next
        
        curr.next = even
        
        return head
