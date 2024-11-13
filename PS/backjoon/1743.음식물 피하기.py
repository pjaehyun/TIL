import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = -1

    count = 1
    while dq:
        x, y = dq.popleft()
        
        for nx, ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = -1
                dq.append((nx, ny))
    return count


answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))
print(answer)