# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # maintain a min_so_far and a max_so_far
        # in that case, keep track of such values and make sure the 
        # current node is within range
        
        # if it isn't, then you return false
        # otherwise, keep dfsing down
        # both paths need to be correct

        def dfs(root, min_so_far, max_so_far):
            if not root:
                return True
            
            if min_so_far < root.val < max_so_far:
                return dfs(root.left, min_so_far, root.val) and dfs(root.right, root.val, max_so_far)
            
            return False
        
        return dfs(root, float('-inf'), float('inf'))