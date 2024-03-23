import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
    dq = deque([(i, j)])
    melting = deque()
    while dq:
        x, y = dq.popleft()
        melt_count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                else:
                    melt_count += 1
        if melt_count:
            melting.append((x, y, melt_count))
    return melting

answer = 0
while True:
    count = 0 
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                count += 1
                visited[i][j] = True
                melt = bfs(i, j)
                while melt:
                    x, y, cnt = melt.popleft()
                    graph[x][y] = max(graph[x][y] - cnt, 0)

    if count == 0:
        print(0)
        break
    if count >= 2:
        print(answer)
        break
    answer += 1