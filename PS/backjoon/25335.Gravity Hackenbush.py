import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, m = map(int, input().split())

coor = [list(map(int, input().split())) for _ in range(n)]

r, g, b = 0, 0, 0
for _ in range(m):
    x, y, c = map(str, input().split())

    if c == "R": r += 1
    elif c == "B": b += 1
    else: g += 1
if r > b:
    print("jhnah917")
elif r < b:
    print("jhnan917")
else:
    if g % 2 == 1:
        print("jhnah917")
    else:
        print("jhnan917")