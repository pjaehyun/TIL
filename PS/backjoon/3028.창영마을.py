import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

s = input().strip()

arr = [1, 0, 0]

for c in s:
    if c == "A":
        arr[0], arr[1] = arr[1], arr[0]
    elif c == "B":
        arr[1], arr[2] = arr[2], arr[1]
    else:
        arr[0], arr[2] = arr[2], arr[0]

for i in range(3):
    if arr[i] == 1:
        print(i+1)