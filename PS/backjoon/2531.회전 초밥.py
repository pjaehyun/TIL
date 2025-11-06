import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]

answer = 0
for l in range(n):
    r = (l + k) % (n+1)
    
    cases = []
    if r < l:
        cases = arr[l:] + arr[:r+1]
    else:
        cases = arr[l:r]
    answer = max(answer, len(set(cases + [c])))
print(answer)