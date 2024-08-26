"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        def po(root):
            if not root:
                return
            for chil in root.children:
                po(chil)
            answer.append(root.val)
        po(root)
        return answer
        