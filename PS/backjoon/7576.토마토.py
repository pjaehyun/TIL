from collections import deque
import queue
M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 1, 0, -1] , [1, 0, -1, 0]

result = 0
dq = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            dq.append([i, j])

while dq:
    x, y = dq.popleft()
    for i in range(4):
        xx, yy = dx[i] + x, dy[i] + y
        if 0 <= xx < N and 0 <= yy < M and tomato[xx][yy] == 0:
            tomato[xx][yy] = tomato[x][y] + 1
            dq.append([xx, yy])


for t in tomato:
    if 0 in t:
        print(-1)
        exit(0)
    result = max(result, max(t))

print(result - 1)