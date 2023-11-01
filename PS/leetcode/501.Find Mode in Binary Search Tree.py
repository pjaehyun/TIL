# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        node_count = defaultdict(int)
        
        def dfs(root):
            node_count[root.val] += 1

            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
        dfs(root)
        
        max_value = max(node_count.values())
        answer = []
        for k, v in node_count.items():
            if v >= max_value:
                answer.append(k)
        return answer
        