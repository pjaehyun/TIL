import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline


while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    print(a + b)