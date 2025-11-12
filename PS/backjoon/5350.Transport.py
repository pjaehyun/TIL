import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, W = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * (W+1) for _ in range(n+1)]
    
        
    for i in range(1, n+1):
        w, v = arr[i-1]
        for j in range(1, W+1):
            if j - w >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][W])