# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # compare the two values
        # if they are different: return False
        # otherwise, propogate further on the subtrees
        # if you hit a null node, then you are done, only if both the nodes are null

        if not p and not q:
            return True
        
        if not p and q or p and not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)