import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

N, A, B = map(int, input().split())
x, y = 1, 1
 
while N:
    x += A
    y += B
 
    if x < y:
        x, y = y, x
 
    if x == y:
        y -= 1
 
    N -= 1
 
 
print(x, y)