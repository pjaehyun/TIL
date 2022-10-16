# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            
            if node.val >= right or node.val <= left:
                return False
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))
        return dfs(root, float(-inf), float(inf))