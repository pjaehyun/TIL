import sys, math
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, K = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if things[i-1][0] <= j:
            dp[i][j] = max(things[i-1][1] + dp[i-1][j - things[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])