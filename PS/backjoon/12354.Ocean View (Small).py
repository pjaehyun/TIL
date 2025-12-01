import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for x in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = float('inf')
    for i in range(n):
        destroyed = i
        prev = arr[i]
        for j in range(i+1, n):
            if prev >= arr[j]:
                destroyed += 1
            else:
                prev = arr[j]
        answer = min(answer, destroyed)
    print("Case #{}: {}".format(x, answer))