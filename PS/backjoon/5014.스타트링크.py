import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

def bfs():
    visited = set()

    dq = deque()

    dq.append((s, 0))
    visited.add(s)

    while dq:
        curr, step = dq.popleft()
        if curr == g:
            return step
        
        if curr + u <= f and curr + u not in visited:
            dq.append((curr + u, step + 1))
            visited.add(curr + u)
        if 0 <= curr - d and curr - d not in visited:
            dq.append((curr - d, step + 1))
            visited.add(curr - d)

    return -1

answer = bfs()
if answer != -1:
    print(answer)
else:
    print("use the stairs")