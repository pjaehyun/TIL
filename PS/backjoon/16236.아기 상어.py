import sys
from collections import deque
sys.setrecursionlimit(10000000)

input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 현재 위치에서 먹을 수 있는 최단거리에 있는 물고기 탐색
def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    dq = deque()
    dq.append((i,j))
    
    res = []

    visited[i][j] = 1

    while dq:
        x, y = dq.popleft()

        for xx, yy in [[x-1,y],[x,y+1],[x+1,y],[x,y-1]]:
            if 0<=xx<N and 0<=yy<N and visited[xx][yy] == 0:
                if sea[i][j] > sea[xx][yy] and sea[xx][yy] != 0:
                    visited[xx][yy] = visited[x][y] + 1
                    res.append((visited[xx][yy] - 1, xx, yy))
                elif sea[i][j] == sea[xx][yy] or sea[xx][yy] == 0:
                    visited[xx][yy] = visited[x][y] + 1
                    dq.append((xx,yy))
    res.sort(key=lambda x:(x[0], x[1], x[2]))

    return (res.pop(0)) if res else -1


answer = 0
start = [0, 0]
comp = [2, 0]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            start[0], start[1] = i, j

while True:
    sea[start[0]][start[1]] = comp[0]
    temp = bfs(start[0], start[1])

    if temp == -1:
        break

    step, x, y = temp
    answer += step
    comp[1] += 1

    if comp[0] == comp[1]:
        comp[0] += 1
        comp[1] = 0
    
    sea[start[0]][start[1]] = 0
    start[0], start[1] = x, y
print(answer)
