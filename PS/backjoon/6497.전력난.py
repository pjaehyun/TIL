import sys
from collections import defaultdict
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(n)}
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX == rY:
            return False
        
        if rX < rY:
            self.uf[rY] = rX
        else:
            self.uf[rX] = rY
        return True

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    graph.sort(key=lambda x:x[2])

    uf = UnionFind(m)

    max_dist = sum([x[2] for x in graph])
    min_dist = 0

    for i in range(n):
        x, y, z = graph[i]
        
        if uf.union(x, y):
            min_dist += z
    print(max_dist - min_dist)