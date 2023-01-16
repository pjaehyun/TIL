import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

G = int(input())
P = int(input())

UF = {x:x for x in range(G+1)}

answer = 0

def find(x):
    if x == -1:
        return -1
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX > rootY:
        UF[rootX] = rootY
    else:
        UF[rootY] = rootX
        

for _ in range(P):
    g = int(input())
    rootG = find(g)
    if rootG != 0:
        answer += 1
        union(rootG, rootG-1)
    else:
        break
print(answer)