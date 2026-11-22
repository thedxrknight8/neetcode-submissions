"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we can use a hashmap 
        # to store nodes that we already created
        # and if we create a node, we store it there
        # then we need to iterate over a current node
        # we dfs and then it would create and link everything 
        # to link, you just take whatever is in the map and link it
        if not node:
            return None
        m = {}

        def dfs(node):
            nonlocal m

            if node.val not in m:
                m[node.val] = Node(node.val, [])
            else:
                return m[node.val]
            
            # we have to initiate a dfs call for each of its neighbors
            for neighbor in node.neighbors:
                m[node.val].neighbors.append(dfs(neighbor))
            
            return m[node.val]
        dfs(node)
        return m[node.val] if node else []
          