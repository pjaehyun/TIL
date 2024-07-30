import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def union(self, x, y):
        
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True


    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

n, m = map(int, input().split())

genders = list(map(str, input().strip().split()))
genders = [None] + genders

graph = []

for _ in range(m):
    s, e, d = map(int, input().split())
    graph.append((s, e, d, genders[s], genders[e]))

graph.sort(key=lambda x:x[2])
uf = UnionFind(n)
answer = 0
for s, e, d, g1, g2 in graph:
    if g1 == g2:
        continue
    
    if uf.union(s, e):
        answer += d

for i in range(2, n+1):
    if uf.find(i) == i:
        answer = -1
        break
print(answer)