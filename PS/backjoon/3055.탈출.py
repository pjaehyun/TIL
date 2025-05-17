import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]

def bfs():
    dq = deque()

    start = [-1, -1]
    end = [-1, -1]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '*':
                dq.append((i, j, 0))
            
            if graph[i][j] == "S":
                start = [i, j]
            
            if graph[i][j] == "D":
                end = [i, j]
    dq.append((start[0], start[1], 0))
    while dq:
        for _ in range(len(dq)):
            x, y, step = dq.popleft()
            if [x,y] == end:
                return step

            if graph[x][y] == "*":
                for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny] == '.':
                        graph[nx][ny] = "*"
                        dq.append((nx, ny, 0))
            else:
                for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny] != "*" and graph[nx][ny] != "X" and graph[nx][ny] != "S":
                        graph[nx][ny] = "S"
                        dq.append((nx, ny, step+1))
    return 0

answer = bfs()

print(answer) if answer else print("KAKTUS")
