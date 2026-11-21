# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = float('-inf')

        def dfs(node):
            nonlocal ret 

            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            ret = max(left_sum + right_sum + node.val, ret)
        
            return max(0, max(left_sum, right_sum) + node.val)
        
        dfs(root)
        return ret