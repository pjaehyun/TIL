class UnionFind:
    def __init__(self, n):
        self.UF = {x:x for x in range(n)}
    
    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX < rY:
            self.UF[rY] = rX
        else:
            self.UF[rX] = rY
    
    def find(self, x):
        if self.UF[x] != x:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i+1, n):
                edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()
        uf = UnionFind(n)
        answer = 0
        for dist, a, b in edges:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                answer += dist
        return answer