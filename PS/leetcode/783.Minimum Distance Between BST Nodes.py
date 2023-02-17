# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        answer = inf
        prev = None

        def inorder(root):
            nonlocal answer, prev
            if not root:
                return
            inorder(root.left)
            if prev is not None:
                answer = min(answer, root.val - prev)
            prev = root.val
            inorder(root.right)
        inorder(root)
        return answer