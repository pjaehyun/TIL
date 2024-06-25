# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        temp = 0
        def order(root):
            nonlocal temp
            if not root:
                return
            order(root.right)
            temp += root.val
            root.val = temp
            order(root.left)
        order(root)
        return root