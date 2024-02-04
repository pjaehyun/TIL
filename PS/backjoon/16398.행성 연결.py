import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x  for x in range(1, n+1)}
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if rootX < rootY:
            self.uf[rootY] = rootX
        else:
            self.uf[rootX] = rootY
        return True

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

n = int(input())

mst = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if i == j:
            continue
        mst.append((i+1, j+1, temp[j]))
mst.sort(key=lambda x:x[2])

uf = UnionFind(n)

answer = 0

for x, y, d in mst:
    if uf.union(x, y):
        answer += d

print(answer)