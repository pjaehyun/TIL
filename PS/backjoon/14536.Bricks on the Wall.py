import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = [list(map(int, input().split())) for _ in range(n)]

    T = sum([x[0] for x in arr])
    W = sum([x[1] for x in arr])
    dp = [-1] * (T+1)
    dp[0] = 0

    for i in range(n):
        for j in range(T, arr[i][0]-1, -1):
            if dp[j-arr[i][0]] != -1:
                dp[j] = max(dp[j], dp[j-arr[i][0]] + arr[i][1])
    
    for i in range(T+1):
        if dp[i] >= W-i:
            print(i)
            break