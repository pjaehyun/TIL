import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append((x, y, 0))

    while dq:
        x, y, step = dq.popleft()
        if (r2, c2) == (x, y):
            return step
        for nx, ny in [(x-2,y-1),(x-2,y+1),(x,y-2),(x,y+2),(x+2,y-1),(x+2,y+1)]:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, step+1))
    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[False] * n for _ in range(n)]
visited[r1][c1] = True
print(bfs(r1, c1))