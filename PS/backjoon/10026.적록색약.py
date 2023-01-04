# 첫번째 풀이(적록색약일때와 아닐때 dfs를 나눠서 풀이)
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

colors = [list(input().strip()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
answer1 = 0
answer2 = 0

def dfs1(x, y):
    for xx, yy in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
        if 0 <= xx < N and 0 <= yy < N and colors[xx][yy] == colors[x][y] and not visited1[xx][yy]:
            visited1[xx][yy] = True
            dfs1(xx, yy)

def dfs2(x, y):
    for xx, yy in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
        if 0 <= xx < N and 0 <= yy < N and ((colors[x][y] == colors[xx][yy]) or (colors[x][y] == 'R' and colors[xx][yy] == 'G') or (colors[x][y] == 'G' and colors[xx][yy] == 'R')) and not visited2[xx][yy]:
            visited2[xx][yy] = True
            dfs2(xx, yy)

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            answer1 += 1
            dfs1(i, j)
        if not visited2[i][j]:
            answer2 += 1
            dfs2(i, j)
print(answer1, answer2)

# 두번째 풀이(적록색약의 그래프를 수정하여 dfs하나로 풀이)
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

colors = [list(input().strip()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
answer1 = 0


red_green = [[z if z != 'G' else 'R' for z in x] for x in colors]
visited2 = [[False] * N for _ in range(N)]
answer2 = 0

def dfs1(x, y, graph, visited):
    for xx, yy in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
        if 0 <= xx < N and 0 <= yy < N and graph[xx][yy] == graph[x][y] and not visited[xx][yy]:
            visited[xx][yy] = True
            dfs1(xx, yy, graph, visited)

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            answer1 += 1
            dfs1(i, j, colors, visited1)
        if not visited2[i][j]:
            answer2 += 1
            dfs1(i, j, red_green, visited2)
print(answer1, answer2)