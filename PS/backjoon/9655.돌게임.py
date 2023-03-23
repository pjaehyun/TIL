import sys
input = sys.stdin.readline

N = int(input())

answer = ["CY","SK"]

dp = [0] * (1001)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)

print(answer[dp[N] % 2])