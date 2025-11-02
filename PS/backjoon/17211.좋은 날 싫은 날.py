import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, f = map(int, input().split())


g_g, g_b, b_g, b_b = map(float, input().split())

if f == 0:
    good = g_g
    bad = g_b
else:
    good = b_g
    bad = b_b

for i in range(n-1):
    g = good
    b = bad

    good = (g * g_g) + (b * b_g)
    bad = (g * g_b) + (b * b_b)

print(int(round(good * 1000)))
print(int(round(bad * 1000)))

