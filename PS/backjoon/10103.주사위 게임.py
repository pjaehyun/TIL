import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

c, s = 100, 100

for _ in range(n):
    x, y = map(int, input().split())

    if x > y:
        s -= x
    elif y > x:
        c -= y
print(c)
print(s)