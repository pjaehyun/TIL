import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

X, Y = 0, 0

for _ in range(n):
    m = input().strip()
    if m == "D":
        X += 1
    else:
        Y += 1
    if abs(X-Y) >= 2:
        break
print("{}:{}".format(X,Y))