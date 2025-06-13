import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

def bs(l, r, x):
    
    while l < r:
        mid = (l + r) // 2
        
        if arr[mid] < d:
            l = mid + 1
        else:
            r = mid
    if l >= n or arr[l] != x: return -1
    return l

for _ in range(m):
    d = int(input())
    print(bs(0, n, d))