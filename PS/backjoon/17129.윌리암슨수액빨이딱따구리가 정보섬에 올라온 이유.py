import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [input().strip() for _ in range(n)]

def bfs(x, y):
    dq = deque()
    dq.append((x, y, 0))

    visited = [[False] * m for _ in range(n)]
    
    visited[x][y] = True

    while dq:
        x, y, step = dq.popleft()
        if graph[x][y] != '0' and graph[x][y] != '2':
            return step

        for nx, ny in [(x+1, y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != '1':
                visited[nx][ny] = True
                dq.append((nx, ny, step+1))
    return -1

start = None
for i in range(n):
    if start:
        break
    for j in range(m):
        if graph[i][j] == '2':
            start = [i, j]
            break

answer = bfs(start[0], start[1])
if answer != -1:
    print("TAK")
    print(answer)
else:
    print("NIE")
