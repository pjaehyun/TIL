import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline


n, m = map(int, input().split())

n = n * 100
if n >= m:
    print("Yes")
else:
    print("No")