N = int(input())

dp = [[0, 0, 0] for _ in range(1001)]

for i in range(1, N + 1):
    r, g, b = map(int, input().split())
    
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r # Red를 칠했을 때 최솟값
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g # Green을 칠했을 때 최솟값
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b # Blue를 칠했을 때 최솟값

print(min(dp[N]))