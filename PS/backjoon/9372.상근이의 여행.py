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
    
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    uf = UnionFind(n)
    step = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if uf.union(a, b):
            step += 1
    print(step)