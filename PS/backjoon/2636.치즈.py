import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def is_touch(x, y):
    if air[x-1][y] == True or air[x][y-1] == True or air[x+1][y] == True or air[x][y+1] == True:
        return True
    return False

def spreads(x, y):
    air[x][y] = True
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 and not air[nx][ny]:
            spreads(nx, ny)

def dfs(x, y):
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            if is_touch(nx, ny):
                graph[nx][ny] = 0
                dfs(nx, ny)
def count_cheese():
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                res += 1
    return res

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

time = 0
an_hour = 0
while True:
    count = count_cheese()

    if count == 0:
        break

    air = [[False] * m for _ in range(n)]
    spreads(0, 0)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and is_touch(i,j):
                graph[i][j] = 0
                dfs(i, j)
    an_hour = count
    time += 1
print(time)
print(an_hour)