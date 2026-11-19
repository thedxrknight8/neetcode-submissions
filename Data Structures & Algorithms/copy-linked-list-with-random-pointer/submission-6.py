"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # iterate through the linked list
        # create a map to store nodes that you create
        # then reuse nodes that you come across that have been created
        # and then point everything together with random and next

        # for instance

        # create {3: ListNode(3)}
        # then take that node and create the new nodes (unless null)
        # {3: ListNode(3), 7: ListNode(7), 4: ListNode(4)} 
        # then point to those new nodes 
        if head is None:
            return None
        nodes = {}
        nodes[head] = Node(head.val, None)
        dummy = Node(0, nodes[head], None)

        while head:
            if head.next:
                if head.next not in nodes:
                    nodes[head.next] = Node(head.next.val, None, None)
                nodes[head].next = nodes[head.next]
            else:
                nodes[head].next = None

            if head.random:
                if head.random not in nodes:
                    nodes[head.random] = Node(head.random.val, None, None)
                nodes[head].random = nodes[head.random]
            else:
                nodes[head].random = None

            head = head.next
        return dummy.next

            
