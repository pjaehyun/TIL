import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

if n < 4:
    if n % 2 != 0:
        print("CY")
    else: print("SK")
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = min(dp[i-1] + 1, dp[i-3] + 1)
    if dp[n] % 2 != 0:
        print("CY")
    else:
        print("SK")