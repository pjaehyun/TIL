# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        leftmost = None

        while dq:
            curr = dq.popleft()

            leftmost = curr.val

            if curr.right:
                dq.append(curr.right)
            if curr.left:
                dq.append(curr.left)
        return leftmost