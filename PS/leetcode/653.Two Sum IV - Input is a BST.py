# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
answer = []
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []
        return dfs(root, result, k)

def dfs(root, lst, val):
    if not root:
        return False
    
    if (val - root.val) in lst:
        return True
    
    lst.append(root.val)
    return dfs(root.left, lst, val) or dfs(root.right, lst, val)