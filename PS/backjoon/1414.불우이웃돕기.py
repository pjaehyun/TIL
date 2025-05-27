import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(n)}
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry: return False

        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True

n = int(input())

computers = [input().strip() for _ in range(n)]

mst = []

total = 0
for i in range(n):
    for j in range(n):
        cable = 0
        if 97 <= ord(computers[i][j]) <= 122:
            cable = ord(computers[i][j]) - 96
        elif 65 <= ord(computers[i][j]) <= 90:
            cable = ord(computers[i][j]) - 38
        
        total += cable
        if i == j or cable == 0: continue

        mst.append((cable, i, j))

mst.sort()

uf = UnionFind(n)

distance = 0
for c, a, b in mst:
    if uf.union(a, b):
        distance += c

parent = 0
for i in range(n):
    parent += uf.find(i)

if parent != 0:
    print(-1)
else: print(total - distance)