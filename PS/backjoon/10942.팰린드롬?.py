import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0] * (n) for _ in range(n)]

for i in range(n):
    for j in range(n-i):
        k = j + i
        if j == k:
            dp[j][k] = 1
        elif arr[j] == arr[k]:
            if j + 1 == k:
                dp[j][k] = 1
            elif dp[j+1][k-1] == 1:
                dp[j][k] = 1
m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])