# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if the min along a certain path isn't greater than that node in
        # time, then that node is a good node
        
        # you can calculate the max by providing that value through dfs
        # function

        # dfs(node, max_so_far=root.val)
        # if node.val < max_so_far: return dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        # otherwise, if node.val >= max_so_far: return 1 + dfs(node.right, node.val) + dfs(node.left, node.val)

        def dfs(node, max_so_far):
            if not node:
                return 0
            
            if node.val < max_so_far:
                return dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
            
            if node.val >= max_so_far:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            
        
        return dfs(root, float('-inf'))