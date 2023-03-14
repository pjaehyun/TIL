# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def order(root, sub):
            nonlocal answer
            if not root.left and not root.right:
                answer += int(sub)
                return
            if root.left:
                order(root.left, sub + str(root.left.val))
            if root.right:
                order(root.right, sub+ str(root.right.val))
        order(root, str(root.val))
        return answer