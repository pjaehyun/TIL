# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_subtree = deque([root.left])
        right_subtree = deque([root.right])
        
        while left_subtree and right_subtree:
            left = []
            right = []
            for _ in range(len(left_subtree)):
                node = left_subtree.popleft()
                if node:
                    left.append(node.val)
                    left_subtree.append(node.left)
                    left_subtree.append(node.right)
                else:
                    left.append(-101)
            
            for _ in range(len(right_subtree)):
                node = right_subtree.popleft()
                if node:
                    right.append(node.val)
                    right_subtree.append(node.left)
                    right_subtree.append(node.right)
                else:
                    right.append(-101)
            if left != right[::-1]:
                return False
        return True
                