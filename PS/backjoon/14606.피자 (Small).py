import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = dp[i-1] + (i//2)
print(dp[n] + dp[n-1])