import sys

input = sys.stdin.readline

N = int(input())

dp = [[0] * 11 for _ in range(N)]

for i in range(1, 11):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(1, 11):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(sum(dp[-1]) % 10007)