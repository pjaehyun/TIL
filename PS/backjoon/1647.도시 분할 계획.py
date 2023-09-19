import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.UF = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX == rY:
            return True
        
        if rX < rY:
            self.UF[rY] = rX
        else:
            self.UF[rX] = rY
        
        return False
    
    def find(self, x):
        if self.UF[x] != x:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]
    
n, m = map(int, input().split())

edges = []
uf = UnionFind(n)

for _ in range(m):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x:x[2])

max_distance = 0

answer = 0

for a, b, d in edges:
    if not uf.union(a, b):
        answer += d
        max_distance = max(max_distance, d)
print(answer - max_distance)