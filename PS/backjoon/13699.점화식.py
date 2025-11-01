import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[0] = 1

for i in range(1, n+1):
    for j in range(i):
        dp[i] += dp[i-j-1] * dp[j]
print(dp[n])