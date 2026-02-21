import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

w, h = map(int, input().split())

print(round(w*h/2, 1))