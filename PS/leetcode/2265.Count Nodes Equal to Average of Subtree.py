# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        answer = 0

        def dfs(node):
            nonlocal answer

            if not node:
                return 0, 0
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            if curr_sum // curr_count == node.val:
                answer += 1
            
            return curr_sum, curr_count
        
        dfs(root)
        return answer