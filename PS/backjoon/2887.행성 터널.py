import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.UF = {x:x for x in range(n)}
    
    def find(self, x):
        if self.UF[x] != x:
            self.UF[x] = self.find(self.UF[x])
        
        return self.UF[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if rootX < rootY:
            self.UF[rootY] = rootX
        else:
            self.UF[rootX] = rootY
        return True

n = int(input())

x_planets = []
y_planets = []
z_planets = []
edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    x_planets.append((x, i))
    y_planets.append((y, i))
    z_planets.append((z, i))

x_planets.sort(), y_planets.sort(), z_planets.sort()

for item in x_planets, y_planets, z_planets:
    for i in range(1, n):
        d1, a = item[i-1]
        d2, b = item[i]
        edges.append((a, b, abs(d1-d2)))
edges.sort(key=lambda x:x[2])

uf = UnionFind(n)
answer = 0

for i in range(len(edges)):
    if uf.union(edges[i][0], edges[i][1]):
        answer += edges[i][2]
print(answer)