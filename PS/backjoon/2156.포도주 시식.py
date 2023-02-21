N = int(input())

graph = [int(input()) for _ in range(N)]

graph = [0] + graph
dp = [0] * (N+1)
dp[1] = graph[1]

if N > 1:
    dp[2] = graph[1] + graph[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-1], dp[i-3] + graph[i-1] + graph[i], dp[i-2] + graph[i])
print(dp[-1])
    