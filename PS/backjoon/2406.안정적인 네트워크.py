import sys
from collections import defaultdict, deque
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

        if rx == ry:
            return False
        
        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True

n, m = map(int, input().split())
uf = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    uf.union(x, y)

graph = [list(map(int, input().split())) for _ in range(n)]

network = []

for i in range(1, n):
    for j in range(i+1, n):
        network.append((graph[i][j], i+1, j+1))
network.sort()

answer = [0, 0, []]
for c, x, y in network:
    if uf.union(x, y):
        answer[0] += c
        answer[1] += 1
        answer[2].append((x, y))

print(answer[0], answer[1])

for x, y in answer[2]:
    print(x, y)