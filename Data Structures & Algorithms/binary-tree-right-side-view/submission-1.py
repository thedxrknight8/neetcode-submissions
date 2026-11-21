# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ret = []

        while q:
            rightSide = None
            n = len(q)

            for _ in range(n):
                rightSide = q.popleft()
                if rightSide.left:
                    q.append(rightSide.left)
                if rightSide.right:
                    q.append(rightSide.right)
            
            ret.append(rightSide.val)

        return ret
