import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(1, n+1)}
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rX = self.find(x)
        rY = self.find(y)

        if rX == rY:
            return False
        
        if rX < rY:
            self.uf[rY] = rX
        else:
            self.uf[rX] = rY
        return True

n, m = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(m)]
lst.sort(key=lambda x:x[2])

total_cost = sum(x[2] for x in lst)

uf = UnionFind(n)
minimum_cost = 0
for i in range(m):
    a, b, c = lst[i]

    if uf.union(a, b):
        minimum_cost += c

check = True
root = 0
for i in range(1, n+1):
    find = uf.find(i)
    if root != 0 and root != find:
        check = False
        break
    root = find
if not check:
    print(-1)
else:
    print(total_cost - minimum_cost)