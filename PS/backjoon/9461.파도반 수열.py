T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0 for _ in range(101)]
    dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7], dp[8], dp[9], dp[10] = 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
    if N <= 10:
        print(dp[N])
        continue
    for i in range(11, N+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[N])