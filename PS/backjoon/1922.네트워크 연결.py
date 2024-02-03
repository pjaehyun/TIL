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
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if rootX < rootY:
            self.uf[rootY] = rootX
        else:
            self.uf[rootX] = rootY
        return True

n = int(input())
m = int(input())

arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x:x[2])

answer = 0
uf = UnionFind(n)

for i in range(len(arr)):
    a, b, c = arr[i]
    if uf.union(a, b):
        answer += c
print(answer)