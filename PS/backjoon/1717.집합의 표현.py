import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

UF = {x:x for x in range(N+1)}

def find(x):
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX < rootY:
        UF[rootY] = rootX
    else:
        UF[rootX] = rootY

for _ in range(M):
    command, x, y = map(int, input().split())
    if command == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
