# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nodes = defaultdict(list)

        def order(root, level):
            nonlocal nodes
            if not root:
                return
            nodes[level].append(root.val)
            
            order(root.left, level + 1)
            order(root.right, level + 1)

        order(root, 0)
        
        answer = []

        for k, v in nodes.items():
            if k % 2 != 0:
                answer.append(v[::-1])
            else: answer.append(v)
        return answer