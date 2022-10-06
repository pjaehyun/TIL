import sys
sys.setrecursionlimit(1000000)

graph = []
dx, dy = [0, 1, 0, -1, -1, -1, +1, +1], [1, 0, -1, 0, -1, +1, +1, -1]

def dfs(x, y):
    graph[x][y] = 0

    for i in range(8):
        xx, yy = dx[i] + x, dy[i] + y
        if xx <= -1 or xx >= len(graph) or yy <= -1 or yy >= len(graph[0]) or graph[xx][yy] == 0:
            continue
        dfs(xx, yy)

while True:
    w, h = map(int, input().split())
    answer = 0
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                answer += 1
                dfs(i, j)
    print(answer)

