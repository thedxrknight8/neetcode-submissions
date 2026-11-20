# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # merge every two lists into one list
        # pop off the next two (if there are two)
        # then, merge them using simple linked list traversal

        # then add back the list
        # and then merge again
        # at the end, replace `lists` with `mergedLists`

        if not lists:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # do you NOT have two available?

                if len(lists) - i < 2:
                    mergedLists.append(lists[i])
                    break
                
                curr = ListNode(0, None)
                dummy = curr
                l1 = lists[i]
                l2 = lists[i + 1]

                while l1 and l2:
                    if l1.val <= l2.val: 
                        dummy.next = l1
                        l1 = l1.next
                        dummy = dummy.next
                    else:
                        dummy.next = l2
                        l2 = l2.next
                        dummy = dummy.next
                
                while l1:
                    dummy.next = l1
                    l1 = l1.next
                    dummy = dummy.next
                
                while l2:
                    dummy.next = l2
                    l2 = l2.next
                    dummy = dummy.next
                # test = curr
                # test = test.next
                # while test:
                #     print(test.val)
                #     test = test.next
                mergedLists.append(curr.next)
                # print(" ")
            lists = mergedLists
        
        return lists[0] 
        