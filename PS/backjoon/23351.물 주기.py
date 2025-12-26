import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k, a, b = map(int, input().split())

hq = [k for _ in range(n)]
days = 0
while hq[0] > 0:

    for i in range(a):
        curr = heapq.heappop(hq)
        curr += b
        heapq.heappush(hq, curr)

    for i in range(n):
        hq[i] -= 1
    days += 1
print(days)