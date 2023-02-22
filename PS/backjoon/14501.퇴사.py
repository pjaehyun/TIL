N = int(input())

schedule = []

for _ in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + schedule[i][0] > N:
        dp[i] = dp[i+1]
    else: 
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i+schedule[i][0]])
print(dp[0])