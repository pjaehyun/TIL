# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 첫번째 풀이
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_nodes = []
        q_nodes = []
        def preOrder(root, nodes):
            if not root:
                nodes.append(None)
                return
            nodes.append(root.val)
            preOrder(root.left, nodes)
            preOrder(root.right, nodes)
        preOrder(p, p_nodes)
        preOrder(q, q_nodes)
        
        if p_nodes == q_nodes:
            return True
        return False
    
# 두번째 풀이
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
