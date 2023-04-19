# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(root, count, way):
            nonlocal answer

            answer = max(answer, count)
            
            if root.left:
                if way != 'left':
                    dfs(root.left, count+1, 'left')
                else:
                    dfs(root.left, 1, 'left')
            if root.right:
                if way != 'right':
                    dfs(root.right, count+1, 'right')
                else:
                    dfs(root.right, 1, 'right')
        dfs(root, 0, 'root')
        return answer
        