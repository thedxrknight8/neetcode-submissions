# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # by performing an in-order traversal, you would iterate 
        # IN-ORDER
        # so then you would get the smallest then the 2nd, 3rd

        # so you would get the smallest element first
        # then the second smallest, third smallest
        # and you can add these to an array

        inorder_traversal = []

        def dfs(node):
            nonlocal inorder_traversal

            if not node:
                return
            
            dfs(node.left)
            inorder_traversal.append(node)
            dfs(node.right)
        
        dfs(root)

        return inorder_traversal[k - 1].val

