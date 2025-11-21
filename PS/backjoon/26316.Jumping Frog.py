import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

for x in range(n):
    c, d = map(int, input().split())

    r = input().strip()

    dp = [float('inf')] * c
    dp[0] = 0

    for i in range(1, c):
        for j in range(1, d+2):
            if r[i] == 'X': continue
            if i >= j:
                dp[i] = min(dp[i], dp[i-j]+1)
    print(f'Day #{x+1}')
    print(c, d)
    print(r)
    if dp[c-1] == float('inf'): print(0)
    else: print(dp[c-1])
    print()