# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result = []
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global result
        preOrder(root, targetSum)
        
        if targetSum in result:
            result.clear()
            return True
        else:
            result.clear()
            return False

def preOrder(root, target):
    global result
    if root == None:
        return
    
    if root.left == None and root.right == None and target == root.val:
        result.append(root.val)

    if root.left != None:
        root.left.val += root.val
    preOrder(root.left, target)

    if root.right != None:
        root.right.val += root.val
    preOrder(root.right, target)