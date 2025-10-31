import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 0:
    print(0)
else:
    arr = list(map(int, input().split()))

    prev = 0
    answer = 1

    for i in range(n):
        if prev + arr[i] <= m:
            prev += arr[i]
        else:
            answer += 1
            prev = arr[i]
    print(answer)