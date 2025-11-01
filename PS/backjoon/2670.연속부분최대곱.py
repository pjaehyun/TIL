import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

arr = [float(input()) for _ in range(n)]

for i in range(1, n):
    arr[i] = max(arr[i], arr[i] * arr[i-1])
print("%.3f"%max(arr))