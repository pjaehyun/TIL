import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k, m = map(int, input().split())

idx = 0

arr = [i+1 for i in range(n)]

d = 1

count = 0

while arr:
    if d == 1:
        curr = (idx + k - 1) % len(arr)
    else:
        curr = (idx - k) % len(arr)
    print(arr.pop(curr))
    idx = curr

    count += 1

    if count == m:
        d ^= 1
        count = 0