class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False
        
        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        uf = UnionFind(n)
        answer = None

        for x, y in edges:
            if not uf.union(x, y):
                answer = [x, y]
        return answer
            