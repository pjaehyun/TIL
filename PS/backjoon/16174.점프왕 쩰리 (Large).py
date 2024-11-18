import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()
        if (x, y) == (n-1, n-1):
            return "HaruHaru"
        for nx, ny in [(x+graph[x][y], y), (x, y+graph[x][y])]:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
    return "Hing"

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

print(bfs(0, 0))