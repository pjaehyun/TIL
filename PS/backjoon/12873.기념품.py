import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

arr = [x for x in range(1, n+1)]
prev = 0
for i in range(1, n):
    t = len(arr)
    loud = i**3

    idx = ((prev + loud % t -1) + t) % t
    prev = idx
    arr.pop(idx)
print(arr[0])