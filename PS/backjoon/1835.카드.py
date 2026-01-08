import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

dq = deque([i for i in range(n)])

answer = [0] * n

count = 1
while dq:
    for _ in range(count):
        curr = dq.popleft()
        dq.append(curr)
    idx = dq.popleft()
    answer[idx] = count
    count += 1
print(*answer)
