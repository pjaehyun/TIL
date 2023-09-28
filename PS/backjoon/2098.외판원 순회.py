import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())

routes = []

for _ in range(n):
    routes.append(list(map(int, input().split())))

dp = [[None] * (1 << n) for _ in range(n)]

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if routes[x][0]:
            return routes[x][0]
        else:
            return INF
    
    if dp[x][visited] != None:
        return dp[x][visited]

    cost = INF
    for i in range(1, n):
        if not routes[x][i] or visited & (1 << i):
            continue
        cost = min(cost, dfs(i, visited | (1 << i)) + routes[x][i])
    dp[x][visited] = cost
    return dp[x][visited]
    
print(dfs(0, 1))