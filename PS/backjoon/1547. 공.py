import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

M = int(input())
tmp = 1
for i in range(M):
    a, b = map(int,input().split())
    if tmp == a:
        tmp = b
    elif tmp == b:
        tmp = a
print(tmp)