import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())

routes = []

for _ in range(n):
    routes.append(list(map(int, input().split())))

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
        if not routes[x][i]:
            continue
        if visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + routes[x][i])
    return dp[x][visited]
    
print(dfs(0, 1))