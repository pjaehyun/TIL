import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)

visited = [[False] * m for _ in range(n)]
answer = 0

def dfs(x, y):
    global answer
    if graph[x][y] == 'P':
        answer += 1

    for i in range(4):
        xx, yy = dx[i] + x, dy[i] + y
        if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and graph[xx][yy] != 'X':
            visited[xx][yy] = True
            dfs(xx, yy)

visited[start[0]][start[1]] = True
dfs(start[0], start[1])

if answer == 0:
    print("TT")
else: print(answer)