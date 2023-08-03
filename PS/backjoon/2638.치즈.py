import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs():
    dq = deque()
    visited = [[False] * m for _ in range(n)]
    dq.append((0, 0))
    visited[0][0] = True

    while dq:
        x, y = dq.popleft()
        for xx, yy in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
            if 0<=xx<n and 0<=yy<m and not visited[xx][yy]:
                if graph[xx][yy] >= 1:
                    graph[xx][yy] += 1
                else:
                    visited[xx][yy] = True
                    dq.append((xx, yy))

answer = 0

while True:
    bfs()
    flag = False

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = True
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if flag:
        answer += 1
    else:
        break
print(answer)