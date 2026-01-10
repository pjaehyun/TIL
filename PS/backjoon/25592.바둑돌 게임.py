import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())
stones = 0 
k = 1

while stones <= n:
    stones += k

    k += 1

if k % 2 == 0:
    print(stones - n)
else:
    print(0)