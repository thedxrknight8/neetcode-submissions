# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # scan k elements 
        # reverse those elements
        # maintain the next pointer (the element right after the last node in the reversal sect) because you need to point the last thing to that element
        # then just move one node ahead to get to the next set of possible k elements
        # scan to see if there is k elements, if there isn't leave it
        # otherwise, perform reversal

        # set dummy = ListNode(0, head)
        # groupPrev = dummy
        # then when you reverse, set groupPrev.next = last element
        # then groupPrev = first element 
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while head:
            k_temp = 0
            curr = head

            while curr and k_temp < k:
                curr = curr.next
                k_temp += 1
            
            if k_temp < k:
                break
            
            newPrev = head
            prev = None
            for _ in range(k):
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            groupPrev.next = prev
            groupPrev = newPrev
            groupPrev.next = head
        
        return dummy.next




        