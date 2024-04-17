class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.ans = None
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, path):
        if not root:
            return

        path.append(chr(root.val + ord('a')))

        if not root.left and not root.right:
            rev_path = ''.join(path[::-1])
            if self.ans is None or rev_path < self.ans:
                self.ans = rev_path

        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()