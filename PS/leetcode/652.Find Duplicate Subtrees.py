# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = Counter()
        answer = []
        def recursion(root):
            if not root:
                return '' 
            left = recursion(root.left)
            right = recursion(root.right)
            subtree = (root.val, left, right)
            subtrees[subtree] += 1
            if subtrees[subtree] == 2:
                answer.append(root)
            return subtree
        recursion(root)
        return answer