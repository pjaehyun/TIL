# 다른 풀이 참고하여 문제 해결
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -inf

        def dfs(root):
            if not root:
                return 0
            lt, rt = dfs(root.left), dfs(root.right)
            max_val = max(root.val + max(lt, rt), root.val)
            self.answer = max(self.answer, max_val, root.val+lt+rt)
            return max_val
        dfs(root)
        return self.answer