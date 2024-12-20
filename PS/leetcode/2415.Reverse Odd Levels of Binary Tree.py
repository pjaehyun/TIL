class Solution:
    def reverseOddLevels(self, root):
        def DFS(leftChild, rightChild, level):
            if not leftChild or not rightChild:
                return
            if level % 2 == 0:
                leftChild.val, rightChild.val = rightChild.val, leftChild.val
            DFS(leftChild.left, rightChild.right, level + 1)
            DFS(leftChild.right, rightChild.left, level + 1)

        DFS(root.left, root.right, 0)
        return root