import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

cities = [list(map(int, input().split())) for _ in range(N)]
con = [i for i in range(N)]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX > rootY:
        con[rootX] = rootY
    else:
        con[rootY] = rootX

def find(x):
    if x != con[x]:
        con[x] = find(con[x])
    return con[x]

for i in range(N):
    for j in range(N):
        if cities[i][j] == 1:
            union(i, j)

path = list(map(int, input().split()))

start = con[path[0] - 1]
check = True
for i in range(1, M):
    if con[path[i] - 1] != start:
        print("NO")
        check = False
        break

if check:
    print("YES")