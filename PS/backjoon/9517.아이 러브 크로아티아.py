import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

k = int(input())

n = int(input())

arr = [0] * 8

limit = 210

time = 0

idx = k-1

for _ in range(n):
    t, z = map(str, input().split())
    t = int(t)

    time += t

    if time >= limit:
        break

    if z == "T":
        idx = ((idx+1) % 8)
print(idx+1)