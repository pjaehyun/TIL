import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(n+1)}
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

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

n, m, k = map(int, input().split())
station = list(map(int, input().split()))

graph = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x:x[2])
uf = UnionFind(n)
for s in station:
    uf.uf[s] = 0

answer = 0
for u, v, w in graph:
    if uf.union(u, v):
        answer += w
print(answer)