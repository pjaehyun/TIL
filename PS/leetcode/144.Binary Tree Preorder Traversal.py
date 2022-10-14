# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root):
            if root == None:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return result

# Stack
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dq, result = deque([root]), []
        if not root: return []
        
        while dq:
            node = dq.pop()
            if node:
                result.append(node.val)
                if node.right: dq.append(node.right)
                if node.left: dq.append(node.left)
        return result