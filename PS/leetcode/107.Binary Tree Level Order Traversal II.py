# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0))
        result = []
        while queue:
            node, level = queue.popleft()
            if node == None:
                continue
            if node.left != None:  queue.append((node.left,level + 1))
            if node.right != None: queue.append((node.right,level + 1))

            try:
                result[level].append(node.val)
            except:
                result.append([])
                result[level].append(node.val)
        return result[::-1]