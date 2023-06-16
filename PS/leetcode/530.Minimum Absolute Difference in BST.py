# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 첫번째 풀이
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = 100000
        def preorder(root, nodes):
            nonlocal answer
            if not root:
                return
            for n in nodes:
                answer = min(answer, abs(root.val - n))
            preorder(root.left, nodes + [root.val])
            preorder(root.right, nodes + [root.val])
        preorder(root, [])
        return answer
    
# 두번째 풀이
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = float('inf')
        parent = -float('inf')
        def inorder(root):
            nonlocal answer, parent
            if not root:
                return
            inorder(root.left)
            answer = min(answer, abs(root.val - parent))
            parent = root.val
            inorder(root.right)
        inorder(root)
        return answer