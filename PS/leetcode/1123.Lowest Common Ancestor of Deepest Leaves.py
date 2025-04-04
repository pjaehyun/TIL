class Solution(object):
    def lcaDeepestLeaves(self, root):
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        def dfs(node, maxi, length):
            if not node:
                return None
            if maxi - 1 == length:
                return node
            left = dfs(node.left, maxi, length + 1)
            right = dfs(node.right, maxi, length + 1)
            if left and right:
                return node
            return left if left else right
        
        maxi = maxDepth(root)
        return dfs(root, maxi, 0)