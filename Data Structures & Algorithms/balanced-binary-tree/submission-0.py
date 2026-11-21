# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # think about two subtrees: 

        # for 1, the left child and the right child don't necessarily have any correlation
        # like for instance, the dfs call operating on root's right child doesn't have anything
        # to do with the operation on the left child

        # why does this matter? because say both the right child and the left child subtrees are 
        # balanced? but the left subtree has height at most 1 but the right subtree has height at most 3...
        # in that case, it is not balanced
        # so not only do the subtrees themselves have to be balanced
        # the heights have to also be checked and compared to make sure they only differ by one

        def dfs(root):
            if not root:
                return [True, 0]

            isBalancedLeft, heightLeft = dfs(root.left)
            isBalancedRight, heightRight = dfs(root.right)

            return [isBalancedLeft and isBalancedRight and abs(heightLeft - heightRight) <= 1, 1 + max(heightLeft, heightRight)]

        return dfs(root)[0]