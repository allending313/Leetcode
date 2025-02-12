# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        x, y, z = head, head.next, head.next.next

        while z:
            temp = y.next
            y.next = x
            x = y
            y = temp

            z = z.next
            if z:
                z = z.next

        head.next = None
        res = 0

        while x and y:
            res = max(res, x.val + y.val)
            x = x.next
            y = y.next

        return res