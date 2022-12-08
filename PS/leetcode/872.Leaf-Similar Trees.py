# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf = []
        root2_leaf = []
        def order(root, leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
            order(root.left, leaf)
            order(root.right, leaf)
        
        order(root1, root1_leaf)
        order(root2, root2_leaf)
        
        if root1_leaf == root2_leaf:
            return True
        return False