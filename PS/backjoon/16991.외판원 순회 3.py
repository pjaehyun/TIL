import math
import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())

routes = [[0] * n for _ in range(n)]

coor = []

for _ in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))

for i in range(n):
    for j in range(i, n):
        dist = math.sqrt((coor[i][0] - coor[j][0])**2 + (coor[i][1] - coor[j][1])**2)
        routes[i][j] = dist
        routes[j][i] = dist

dp = [[INF] * (1 << n) for _ in range(n)]

def dfs(x, visited):
    
    if visited == (1 << n) - 1:
        if routes[x][0]:
            return routes[x][0]
        else:
            return INF
    
    if dp[x][visited] != INF:
        return dp[x][visited]
    
    for i in range(1, n):
        if not routes[x][i] or (visited & (1 << i)):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | 1 << i) + routes[x][i])
    return dp[x][visited]

print(dfs(0, 1))