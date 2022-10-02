N = int(input())
dp = [0 for x in range(1000001)]

dp[2], dp[3] = 1, 1

for i in range(4, len(dp)):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
        
print(dp[N])
        