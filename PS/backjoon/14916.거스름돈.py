import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

if n < 5:
    if n % 2 != 0:
        print(-1)
    else:
        print(n // 2)
else:
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    dp[2] = 1
    dp[4] = 2

    for i in range(5, n+1):
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)

    print(dp[n])