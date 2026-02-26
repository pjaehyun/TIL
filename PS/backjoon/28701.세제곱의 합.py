import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

print(n*(n+1)//2)
print((n*(n+1)//2)**2)
print(sum([x**3 for x in range(1, n+1)]))