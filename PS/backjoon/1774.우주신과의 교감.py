import sys, math
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        rX, rY = self.find(x), self.find(y)

        if rX == rY:
            return False
        
        if rX < rY:
            self.uf[rY] = rX
        else:
            self.uf[rX] = rY
        return True

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

n, m = map(int, input().split())

spaceships = [list(map(int, input().split())) for _ in range(n)]

graph = []

for i in range(n):
    x1, y1 = spaceships[i]
    for j in range(i+1, n):
        x2, y2 = spaceships[j]
        graph.append((i+1, j+1, math.sqrt(abs(x2-x1)**2 + abs(y2-y1)**2)))

graph.sort(key=lambda x:x[2])
uf = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    uf.union(x, y)

answer = 0.0
for x, y, d in graph:
    if uf.union(x, y):
        answer += d
print(format(answer, ".2f"))