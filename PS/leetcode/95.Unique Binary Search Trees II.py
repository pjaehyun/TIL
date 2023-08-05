# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {}

        def recursion(start, end):
            if (start, end) in dp:
                return dp[(start, end)]
            
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for val in range(start, end+1):
                left_trees = recursion(start, val - 1)
                right_trees = recursion(val+1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(val, left, right)
                        trees.append(root)
            dp[(start, end)] = trees
            return trees
        
        return recursion(1, n)