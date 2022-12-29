import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
answer = 0

def bfs():
    dq = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    dq.append((i, j, k))

    while dq:
        h, x, y = dq.popleft()
        for xx, yy, hh in [[x, y+1, h],[x+1, y, h],[x, y-1, h],[x-1, y, h], [x,y,h+1],[x,y,h-1]]:
            if 0 <= xx < N and 0 <= yy < M and 0 <= hh < H and tomato[hh][xx][yy] == 0:
                tomato[hh][xx][yy] = tomato[h][x][y] + 1
                dq.append((hh, xx, yy))
            
bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            answer = max(answer, tomato[i][j][k])
print(answer-1)