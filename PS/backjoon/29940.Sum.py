import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, s = map(int, input().split())

arr = [int(input()) for _ in range(n)]

l, r = 0, n-1

answer = 0
while l < r:
    
    _sum = arr[l] + arr[r]

    if _sum == s:
        answer += 1
        l += 1
        r -= 1
    elif _sum < s:
        l += 1
    else:
        r -= 1
print(answer)