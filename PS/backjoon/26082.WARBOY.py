import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

a, b, c = map(int, input().split())

print((b // a * 3) * c)