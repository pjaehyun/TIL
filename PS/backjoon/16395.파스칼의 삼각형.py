import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (x+2) for x in range(1, n+1)]

dp[0][1] = 1


for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n-1][k])