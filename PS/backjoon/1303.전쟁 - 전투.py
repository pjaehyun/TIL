import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, team):
    dq = deque()
    dq.append((x, y))

    count = 1
    while dq:
        x, y = dq.popleft()
        
        for nx, ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == team and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                dq.append((nx, ny))
    return count


m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input().strip())

visited = [[False] * m for _ in range(n)]

white = 0
black = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if graph[i][j] == 'W':
                white += bfs(i, j, 'W')**2
            else:
                black += bfs(i, j, 'B')**2
print(white, black)