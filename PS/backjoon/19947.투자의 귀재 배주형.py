import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

h, y = map(int, input().split())

dp = [0] * 11

dp[0] = h

for i in range(1, 11):
    if i-5 >= 0:
        dp[i] = max(dp[i], int(dp[i-5] * 1.35))
    if i-3 >= 0:
        dp[i] = max(dp[i], int(dp[i-3] * 1.2))
    dp[i] = max(dp[i], int(dp[i-1] * 1.05))
print(dp[y])