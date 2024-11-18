import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    dq = deque()
    dq.append((x, 0))
    visited[x] = True

    while dq:
        x, step = dq.popleft()
        if x == m:
            return step
        for nx in [x+1, x-1, x+a, x+b, x-a, x-b, x*a, x*b]:
            if 0<=nx<100001 and not visited[nx]:
                visited[nx] = True
                dq.append((nx, step+1))


a, b, n, m = map(int, input().split())

graph = [0] * 100001
visited = [False] * 100001
print(bfs(n))
