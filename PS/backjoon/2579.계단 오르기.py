N = int(input())
lst = [0 for _ in range(301)]
for i in range(1, N+1):
    lst[i] = int(input())

dp = [0 for _ in range(301)]

dp[1] = lst[1]
dp[2] = lst[1] + lst[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])
print(dp[N])
