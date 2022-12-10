# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_list = []
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            _sum = left + right + root.val
            sum_list.append(_sum)
            return _sum
        total = dfs(root)
        answer = 0
        for s in sum_list:
            answer = max(answer, (total - s) * s)
        return answer % (10**9 + 7)
