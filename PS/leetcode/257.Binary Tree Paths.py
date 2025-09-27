# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        def order(root, path):
            if not root:
                return
            
            path += str(root.val) + '->'

            if not root.left and not root.right:
                answer.append(path[:-2])
                return
                
            order(root.left, path)
            order(root.right, path)
        order(root, "")
        
        return answer