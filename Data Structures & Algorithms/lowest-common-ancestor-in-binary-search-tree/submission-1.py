# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # what are the cases?
        # p is the parent 
        # p and q are children of some higher node
        # q is the parent

        # if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
        # return root as the lowestCommonAncestor

        # otherwise, if p.val < root.val and q.val < root.val -> search left -- other case -> search right
        # if root == p: return root
        # if root == q: return root

        if not root:
            return root

        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root 
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)