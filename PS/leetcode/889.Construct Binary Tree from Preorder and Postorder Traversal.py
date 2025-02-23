class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def makeTree():            
            node = TreeNode(postorder.pop())

            if node.val != preorder[-1]:
                node.right = makeTree() 

            if node.val != preorder[-1]:
                node.left = makeTree()

            preorder.pop()
            return node

        return makeTree()