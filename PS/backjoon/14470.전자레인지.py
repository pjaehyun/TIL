import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    time = -a * c + d + b * e
else:
    time = (b - a) * e

print(time)