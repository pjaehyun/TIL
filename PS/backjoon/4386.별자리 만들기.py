import sys
import math
input = sys.stdin.readline

def find(x):
    if UF[x] != x:
        UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX == rootY:
        return False

    if rootX < rootY:
        UF[rootY] = rootX
    else:
        UF[rootX] = rootY
    return True

n = int(input())

stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
UF = {x:x for x in range(n)}

for i in range(n):
    for j in range(i+1, n):
        distance = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
        edges.append((distance, i, j))

edges.sort()
answer = 0

for i in range(len(edges)):
    distance, a, b = edges[i]
    if union(a, b):
        answer += distance
print(round(answer, 2))