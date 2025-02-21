# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.element = set()
        self.element.add(0)
        root.val = 0

        self.dfs(root.left, root.val, "L")
        self.dfs(root.right, root.val, "R")

        print(self.element)
    def find(self, target: int) -> bool:
        return False if target not in self.element else True
    
    def dfs(self, root, parent, direction):
        if not root:
            return

        if direction == "L": root.val = parent * 2 + 1
        else: root.val = parent * 2 + 2
        
        self.element.add(root.val)
        self.dfs(root.left, root.val, "L")
        self.dfs(root.right, root.val, "R")