# 벽만 부수면 되는줄 알았다가 점프했을 때 도달할 공간이 있어야 된다는걸 늦게 깨달음 
# 그래서 문제 풀이 시간이 굉장히 길어졌다
from collections import deque
def solution(n, m, hole):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    graph = [[0] * m for _ in range(n)]
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    dq = deque()
    
    for x, y in hole:
        graph[x-1][y-1] = 1
    
    dq.append((0, 0, 0))
    
    while dq:
        x, y, w = dq.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w] - 1
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0<=xx<n and 0<=yy<m:
                if graph[xx][yy] == 0 and visited[xx][yy][w] == 0:
                    visited[xx][yy][w] = visited[x][y][w] + 1
                    dq.append((xx, yy, w))
                elif graph[xx][yy] == 1 and w == 0:
                    xxx, yyy = xx+dx[i], yy+dy[i]
                    if 0<=xxx<n and 0<=yyy<m and graph[xxx][yyy]==0:
                        visited[xx][yy][w+1] = visited[x][y][w] + 1
                        dq.append((xx, yy, w+1))
    return -1