import sys
input = sys.stdin.readline

n, m = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.UF = {x: x for x in range(n)}
    
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

uf = UnionFind(n)
is_cycle = False
count = 0
for _ in range(m):
    a, b = map(int, input().split())
    count += 1
    if not uf.union(a, b):
        is_cycle = True
        break
if is_cycle:
    print(count)
else:
    print(0)