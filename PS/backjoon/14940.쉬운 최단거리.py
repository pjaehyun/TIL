import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dq = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            dq.append((i, j))
            answer[i][j] = 0
            visited[i][j] = True
        if graph[i][j] == 0:
            answer[i][j] = 0

while dq:
    x, y = dq.popleft()

    for i in range(4):
        xx, yy = dx[i] + x, dy[i] + y

        if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and graph[xx][yy] == 1:
            answer[xx][yy] = answer[x][y] + 1
            visited[xx][yy] = True
            dq.append((xx, yy))

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()