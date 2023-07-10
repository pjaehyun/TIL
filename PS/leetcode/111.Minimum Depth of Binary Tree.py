# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        answer = float('inf')

        def search(root, level):
            nonlocal answer
            if not root:
                return
            
            if not root.left and not root.right:
                answer = min(answer, level)
            
            search(root.left, level+1)
            search(root.right, level+1)
        search(root, 1)
        return answer