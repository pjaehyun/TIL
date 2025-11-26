import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

q = deque()

for i in range(n-1, -1, -1):
    if a[i] == 0:
        q.append(b[i])

answer = []
for i in range(m):
    q.append(c[i])
    answer.append(q.popleft())
print(*answer)