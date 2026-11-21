# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {inorder[i]: i for i in range(len(inorder))}
        self.shared_index = 0

        def dfs(left, right):
            if left > right:
                return None
            root_idx = positions[preorder[self.shared_index]]
            root = TreeNode(inorder[root_idx], None, None)
            self.shared_index += 1

            left_end = root_idx - 1
            right_start = root_idx + 1

            root.left = dfs(left, left_end)
            root.right = dfs(right_start, right)

            return root
        
        return dfs(0, len(inorder) - 1)

            

        