# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum1, sum2 = 0, 0

        while l1 != None:
            sum1 *= 10 
            sum1 += l1.val
            l1 = l1.next
        
        while l2 != None:
            sum2 *= 10 
            sum2 += l2.val
            l2 = l2.next

        res = ListNode(None)
        cur = res

        for num in str(sum1 + sum2):
            cur.next = ListNode(int(num))
            cur = cur.next

        return res.next        
        
        # #reverse linked list
        # def reverse(node):
        #     if not node or not node.next:
        #         return node
        #     temp = reverse(node.next)
        #     node.next.next = node
        #     node.next = None
        #     return temp
        
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        
        # res, prev = None, None
        
        # carry = 0
        # while l1 or l2:
        #     if l1 and l2:
        #         value = l1.val + l2.val + carry
        #         if value > 9:
        #             carry = 1
        #             value %= 10
        #         else:
        #             carry = 0
                
        #         res = ListNode(value)
        #         res.next = prev
        #         prev = res
        #         l1 = l1.next
        #         l2 = l2.next
            
        #     elif l1:
        #         value = l1.val + carry
        #         if value > 9:
        #             carry = 1
        #             value %= 10
        #         else:
        #             carry = 0
        #         res = ListNode(value)
        #         res.next = prev
        #         prev = res
        #         l1 = l1.next

        #     elif l2:
        #         value = l2.val + carry
        #         if value > 9:
        #             carry = 1
        #             value %= 10
        #         else:
        #             carry = 0
        #         res = ListNode(value)
        #         res.next = prev
        #         prev = res
        #         l2 = l2.next
            
        # if carry:
        #     res = ListNode(1)
        #     res.next = prev
        #     prev = res
        
        # return res
            

