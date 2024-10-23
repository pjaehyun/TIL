class Solution:
    def dfs(self, node):
        if not node: return
        node.val = self.tbl[node.level] - node.parent.childs if node.parent else 0
        self.dfs(node.right)
        self.dfs(node.left)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.parent = None
        root.level = 0
        q = [root]
        self.tbl = defaultdict(int)
        while q:
            node = q.pop()
            node.childs = 0 
            self.tbl[node.level] += node.val
            
            if node.left:
                node.left.parent = node 
                node.left.level = node.level + 1
                node.childs += node.left.val
                q.append(node.left)
            if node.right:
                node.right.parent = node
                node.right.level = node.level + 1
                node.childs += node.right.val
                q.append(node.right)
        self.dfs(root)
        return root