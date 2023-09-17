import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.UF = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX == rY:
            return False

        if rX < rY:
            self.UF[rY] = rX
        else:
            self.UF[rX] = rY
        return True
        
    def find(self, x):
        if self.UF[x] != x:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]
    


v, e = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(e)]

edges.sort(key=lambda x:x[2])
uf = UnionFind(v)
answer = 0

for edge in edges:
    if uf.union(edge[0], edge[1]):
        answer += edge[2]
print(answer)