import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())
cats = list(map(int, input().split()))

cats.sort()

l, r = 0, len(cats) - 1
answer = 0
while l < r:
    if cats[l] + cats[r] <= k:
        l += 1
        r -= 1
        answer += 1
    else:
        r -= 1
print(answer)