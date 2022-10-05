# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        
        level = 1
        queue = deque([root])

        while queue:
            level += 1
            for i in range(len(queue)):
                current = queue.popleft()
                
                if level == depth:
                    current.left = TreeNode(val, left=current.left)
                    current.right = TreeNode(val, right=current.right)
                
                else:
                    queue.append(current.left) if current.left else None
                    queue.append(current.right) if current.right else None
        
        return root if depth > 1 else TreeNode(val, left=root)