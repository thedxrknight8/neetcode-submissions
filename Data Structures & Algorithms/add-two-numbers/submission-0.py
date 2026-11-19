# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_res = 0
        l2_res = 0

        mult = 1
        while l1:
            l1_res += l1.val * mult
            mult *= 10
            l1 = l1.next
        mult = 1
        while l2:
            l2_res += l2.val * mult
            mult *= 10
            l2 = l2.next
        
        res = l1_res + l2_res

        ret = ListNode(0, None)
        dummy = ListNode(0, ret)
        print(res)
        while res > 0 and ret:
            rem = res % 10
            ret.val = rem
            res //= 10
            if res > 0:
                ret.next = ListNode(0, None)
            
            ret = ret.next
        return dummy.next
