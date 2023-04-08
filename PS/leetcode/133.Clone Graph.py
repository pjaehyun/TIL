"""
# Definition for a Node.
class Node
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        dq = deque()
        dq.append(node)

        clone = {node.val: Node(node.val, [])}
        while dq:
            n = dq.popleft()
            curr = clone[n.val]
            for neib in n.neighbors:
                if neib.val not in clone:
                    clone[neib.val] = Node(neib.val, [])
                    dq.append(neib)
                curr.neighbors.append(clone[neib.val])
        return clone[node.val]
