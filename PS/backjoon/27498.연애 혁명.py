import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry: return False

        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x:(-x[3],-x[2]))

uf = UnionFind(n)

mst = 0
remove = 0
for a, b, c, d in graph:
    if d == 1:
        uf.union(a, b)
        mst += c
    else:
        if uf.union(a, b):
            mst += c
        else:
            remove += c
print(remove)
        