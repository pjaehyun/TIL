# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        nodes = []
        def order(root):
            if not root:
                return
            nodes.append(root.val)
            order(root.left)
            order(root.right)
        order(root)
        return len(nodes)