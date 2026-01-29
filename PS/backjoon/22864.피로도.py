import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

A,B,C,M = map(int, sys.stdin.readline().split())

T = 0
DW = 0

for i in range(24):
  if T > M:
    print(0)
  else:
    if T + A <= M:
      T += A
      DW += B
    else:
      if T - C >=0:
        T -= C
      else:
        T = 0
print(DW)