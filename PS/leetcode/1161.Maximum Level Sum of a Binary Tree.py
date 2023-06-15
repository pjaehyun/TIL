# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums = defaultdict(int)

        dq = deque()
        dq.append((root, 1))

        while dq:
            node, level = dq.popleft()
            level_sums[level] += node.val

            if node.left:
                dq.append((node.left, level+1))
            if node.right:
                dq.append((node.right, level+1))
        
        answer = 1
        max_sum = root.val
        for k, v in level_sums.items():
            if v > max_sum:
                max_sum = v
                answer = k
        return answer