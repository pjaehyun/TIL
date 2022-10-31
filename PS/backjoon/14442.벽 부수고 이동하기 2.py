from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for x in range(N)]
visited[0][0][K] = 1

def bfs():
    dq = deque()
    dq.append((0, 0, K))
    while dq:
        x, y, w = dq.popleft()
        
        if x >= N-1 and y >= M-1:
            return visited[x][y][w]

        for xx, yy in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
            if 0 <= xx < N and 0 <= yy < M:
                if graph[xx][yy] == 0 and visited[xx][yy][w] == 0:
                    dq.append((xx, yy, w))
                    visited[xx][yy][w] = visited[x][y][w] + 1
                elif graph[xx][yy] == 1 and visited[xx][yy][w-1] == 0 and w > 0:
                    dq.append((xx, yy, w-1))
                    visited[xx][yy][w-1] = visited[x][y][w] + 1
    return -1
print(bfs())