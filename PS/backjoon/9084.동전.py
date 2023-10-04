import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = [0] + list(map(int, input().split()))
    m = int(input())

    dp = [[1 if j == 0 else 0 for j in range(m+1)] for i in range(n+1)]
    

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j - coins[i] >= 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][m])