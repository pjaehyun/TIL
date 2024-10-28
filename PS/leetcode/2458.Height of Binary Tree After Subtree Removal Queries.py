class Solution(object):
    def __init__(self):
        self.depth = [0] * 100001
        self.levelArr = [0] * 100001
        self.max1 = [0] * 100001
        self.max2 = [0] * 100001

    def height(self, root, level):
        if not root:
            return 0
        
        self.levelArr[root.val] = level
        self.depth[root.val] = 1 + max(self.height(root.left, level + 1), self.height(root.right, level + 1))
        
        if self.max1[level] < self.depth[root.val]:
            self.max2[level] = self.max1[level]
            self.max1[level] = self.depth[root.val]
        elif self.max2[level] < self.depth[root.val]:
            self.max2[level] = self.depth[root.val]
        
        return self.depth[root.val]

    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        self.height(root, 0)

        result = []
        for q in queries:
            level = self.levelArr[q]
            
            result.append((self.max2[level] if self.max1[level] == self.depth[q] else self.max1[level]) + level - 1)
        
        return result