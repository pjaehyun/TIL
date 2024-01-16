import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):

    dq = deque()
    dq.append((x, y))
    graph[x][y] = 1
    area = 1

    while dq:
        cur_x, cur_y = dq.popleft()

        for nx, ny in [(cur_x+1,cur_y),(cur_x,cur_y+1),(cur_x-1,cur_y),(cur_x,cur_y-1)]:
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                dq.append((nx,ny))
                graph[nx][ny] = 1
                area += 1
    return area


m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

area_count = 0
areas = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area_count += 1
            areas.append(bfs(i, j))
print(area_count)
print(*sorted(areas))