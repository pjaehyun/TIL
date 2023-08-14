import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [0] * (100000+1)

dq = deque()
visited = [False] * (100000+1)
dq.append((n, 0))
visited[n] = True

fast = k - n
count = 0

while dq:
    curr, time = dq.popleft()
    visited[curr] = True
    if count > 0 and curr == k and time == fast:
        count += 1

    if curr == k and count == 0:
        fast = time
        count += 1

    for move in [curr+1, curr-1, curr*2]:
        if 0 <= move <= 100000 and not visited[move]:
            dq.append((move, time + 1))

print(fast)
print(count)