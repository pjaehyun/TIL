import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

dp = [0] * 70

dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4

for i in range(4, 70):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

t = int(input())
for _ in range(t):
    n = int(input())

    print(dp[n])