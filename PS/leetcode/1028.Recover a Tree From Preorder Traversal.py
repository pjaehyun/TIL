class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = [(len(node[1]), int(node[2])) for node in re.findall("((-*)(\d+))", traversal)][::-1]

        def makeTree(depth): 
            if not nodes or depth != nodes[-1][0]: return None 

            node = TreeNode(nodes.pop()[1]) 
            node.left = makeTree(depth + 1) 
            node.right = makeTree(depth + 1)

            return node

        return makeTree(0) 