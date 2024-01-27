import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maze = [input().strip() for _ in range(n)]

f_visited = [[0] * m for _ in range(n)]
j_visited = [[0] * m for _ in range(n)]

f_dq = deque()
j_dq = deque()

for i in range(n):
    for j in range(m):
        if maze[i][j] == "J":
            j_dq.append((i, j))
        elif maze[i][j] == "F":
            f_dq.append((i, j))

def bfs():
    while f_dq:
        x, y = f_dq.popleft()
        
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == "." and not f_visited[nx][ny]:
                f_visited[nx][ny] = f_visited[x][y] + 1
                f_dq.append((nx, ny))

    while j_dq:
        x, y = j_dq.popleft()
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return j_visited[x][y] + 1
            if maze[nx][ny] == "." and (not j_visited[nx][ny] and (not f_visited[nx][ny] or f_visited[nx][ny] > j_visited[x][y] + 1)) :
                    j_visited[nx][ny] = j_visited[x][y] + 1
                    j_dq.append((nx, ny))
    return "IMPOSSIBLE"
print(bfs())