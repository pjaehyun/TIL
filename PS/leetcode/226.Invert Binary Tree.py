# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def search(root):
            if not root:
                return root
            search(root.left)
            search(root.right)
            
            root.left, root.right = root.right, root.left
        search(root)
        return root
