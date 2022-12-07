# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 첫번째 풀이
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = []
        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                answer.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sum(answer)


# 두번째 풀이
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root, low, high):
            if not root:
                return 0
            if low <= root.val <= high:
                return root.val + dfs(root.left, low, high) + dfs(root.right, low, high)
            if root.val < low:
                return dfs(root.right, low, high)
            elif root.val > high:
                return dfs(root.left, low, high)
        return dfs(root, low, high)