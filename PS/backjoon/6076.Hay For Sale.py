import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

c, h = map(int, input().split())

bales = [int(input()) for _ in range(h)]

dp = 1
max_mask = (1 << (c+1)) - 1

for b in bales:
    dp = (dp | (dp << b)) & max_mask

for i in range(c, -1, -1):
    if (dp >> i) & 1:
        print(i)
        break