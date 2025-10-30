import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

dp = [0] * 117

dp[0], dp[1], dp[2] = 0, 1, 1

for i in range(3, 117):
    dp[i] = dp[i-1] + dp[i-3]
print(dp[n])