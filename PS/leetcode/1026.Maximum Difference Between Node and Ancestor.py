# 첫번째 풀이
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = []
        def order(root, parent):
            if not root:
                return
            for p in parent:
                answer.append(abs(root.val - p))
            order(root.left, parent + [root.val])
            order(root.right, parent + [root.val])
        
        order(root.left,[root.val])
        order(root.right,[root.val])
        return max(answer)


# 두번째 풀이(시간복잡도 개선)
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def max_diff(root, low, high):
            if not root:
                return high - low
            low = min(low, root.val)
            high = max(high, root.val)

            return max(max_diff(root.left, low, high), max_diff(root.right, low, high))
        
        if not root:
            return
        else: return max_diff(root, root.val, root.val)