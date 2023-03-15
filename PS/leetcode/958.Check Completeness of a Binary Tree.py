# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq = deque([root])

        seen = False
        while dq:
            node = dq.popleft()
            if not node:
                seen = True
                continue
            
            if seen:
                return False

            dq.append(node.left)
            dq.append(node.right)
        return True 