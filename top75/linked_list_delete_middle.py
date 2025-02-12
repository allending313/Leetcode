# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow, fast = head, head.next
        # prev = head

        # if not fast:
        #     head = None

        # while fast:
        #     prev = slow
        #     slow = slow.next
        #     fast = fast.next
        #     if fast:
        #         fast = fast.next
        
        # prev.next = slow.next
        # return head

        temp = slow = fast = ListNode(0)
        temp.next = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return temp.next