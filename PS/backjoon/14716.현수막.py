import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, y):
    for nx, ny in [(x+1,y),(x-1,y),(x,y-1),(x,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]:
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            answer += 1
            graph[i][j] = 0
            dfs(i, j)
print(answer)