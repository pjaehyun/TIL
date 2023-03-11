# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_level(root):
            if not root:
                return 0
            left, right = get_level(root.left), get_level(root.right)
            print(left, right)
            if left < 0 or right < 0 or abs(left - right) > 1: return -1
            return max(left, right) + 1
        return True if get_level(root) >= 0 else False