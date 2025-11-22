import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    l, s = map(int, input().split())

    while stack and stack[-1][1] > s:
        stack.pop()
    
    stack.append((l, s))
print(len(stack))