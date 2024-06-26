# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def inorder(root):
            if root==None: return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        def BST(l, r):
            if l>r: return None
            m=(l+r)//2
            left=BST(l, m-1)
            right=BST(m+1, r)
            return TreeNode(arr[m], left, right)
        
        inorder(root)
        return BST(0, len(arr)-1)