import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
    exit(0)

dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]
print(dp[-1] % 10007)