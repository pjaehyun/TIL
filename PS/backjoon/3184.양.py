import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    sheeps = 0
    wolves = 0

    while dq:
        x, y = dq.popleft()

        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != '#' and not visited[nx][ny]:
                if graph[nx][ny] == "o":
                    sheeps += 1
                elif graph[nx][ny] == "v":
                    wolves += 1
                visited[nx][ny] = True
                dq.append((nx, ny))
    return sheeps, wolves

n, m = map(int ,input().split())
graph = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]

sheeps, wolves = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and not visited[i][j]:
            visited[i][j] = True
            s, w = bfs(i, j)
            if graph[i][j] == "o":
                s += 1
            if graph[i][j] == "v":
                w += 1
            if s > w:
                sheeps += s
            else:
                wolves += w
print(sheeps, wolves)