# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(node):
            res = []
            dq = deque()
            dq.append(node)

            while dq:
                _max = float('-inf')
                for _ in range(len(dq)):
                    curr = dq.popleft()
                    _max = max(_max, curr.val)
                    if curr.left:
                        dq.append(curr.left)
                    if curr.right:
                        dq.append(curr.right)
                res.append(_max)
            return res
        return bfs(root)
        