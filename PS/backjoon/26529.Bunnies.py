import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())
dp = [0] * 46
dp[0] = 1
dp[1] = 1

for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(n):
    x = int(input())

    print(dp[x])