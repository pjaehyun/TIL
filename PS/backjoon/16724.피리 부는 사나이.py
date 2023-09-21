import sys
input = sys.stdin.readline

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
    

n, m = map(int, input().split())

direction = [list(input().strip()) for _ in range(n)]
graph = [[0] * m for _ in range(n)]
uf = UnionFind(n * m)

idx = 0
for i in range(n):
    for j in range(m):
        graph[i][j] = idx
        idx += 1

for i in range(n):
    for j in range(m):
        if direction[i][j] == 'D':
            uf.union(graph[i][j], graph[i+1][j])
        elif direction[i][j] == 'U':
            uf.union(graph[i][j], graph[i-1][j])
        elif direction[i][j] == 'L':
            uf.union(graph[i][j], graph[i][j-1])
        else:
            uf.union(graph[i][j], graph[i][j+1])

answer = set()
for v in uf.UF.values():
    answer.add(uf.find(v))
print(len(answer))
