import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())

arr = ["?"] * n

idx = 0

lucky = True

for i in range(k):
    m, s = map(str, input().split())
    m = int(m)
    
    idx = (idx + n - m) % n
    
    if (arr[idx] != "?" and arr[idx] != s):
        lucky = False
        break

    if arr[idx] != s and s in arr:
        lucky = False
        break
    arr[idx] = s

if lucky:
    answer = [""] * n
    for i in range(n):
        answer[i] = arr[(i+idx)%n]
    print(''.join(answer))
else:
    print("!")