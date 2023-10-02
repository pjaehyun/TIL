import sys
input = sys.stdin.readline

n, t = map(int, input().split())
studies = []

for _ in range(n):
    k, s = map(int, input().split())
    studies.append((k, s))

dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if j - studies[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - studies[i-1][0]] + studies[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])