# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if there is a subtree on the right OR the left, you are good

        # to check for a subtree, you check the current comparison. 
        # then, if equal, you pass a dfs of the corresponding ndoe 
        # otherwise, pass the same node of the subroot
        # to return, 

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root and subRoot or root and not subRoot:
                return False
            
            if root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)

        if not subRoot:
            return True
        if not root:
            return False
        
        if dfs(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            