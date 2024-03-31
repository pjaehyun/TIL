import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y):
    global count
    count += 1
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

max_pucture = 0
picture_count = 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        count = 0
        if not visited[i][j] and graph[i][j] == 1:
            visited[i][j] = True
            dfs(i, j)
            picture_count += 1
        max_pucture = max(max_pucture, count)
print(picture_count)
print(max_pucture)
            