T = int(input())

dp = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    dp[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        for k in range(j, i-1, -1):
            dp[i][j] += dp[i-1][k-1]

for i in range(T):
    N, M = map(int, input().split())
    print(dp[N][M])