"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        answer = Node()
        def recursion(w, h, n, root):
            check = grid[h][w]
            for i in range(h, h+n):
                for j in range(w, w+n):
                    if grid[i][j] != check:
                        root.isLeaf = 0
                        root.val = 1
                        root.topLeft = Node()
                        recursion(w, h, n // 2, root.topLeft)
                        root.topRight = Node()
                        recursion(w + n//2, h, n // 2, root.topRight)
                        root.bottomLeft = Node()
                        recursion(w, h + n//2, n//2, root.bottomLeft)
                        root.bottomRight = Node()
                        recursion(w+ n//2, h + n//2, n//2, root.bottomRight)
                        return
            if check == 1:
                root.isLeaf = 1
                root.val = 1
            else:
                root.isLeaf = 1
                root.val = 0
            
        recursion(0, 0, len(grid), answer)
        return answer    
            