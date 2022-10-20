from collections import deque

N, M = map(int, input().split())

graph = [[int(x) for x in input()] for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

def bfs():
    dq = deque()
    dq.append((0,0,0))

    while dq:
        x, y, w = dq.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if xx < 0 or xx >= len(graph) or yy < 0 or yy >= len(graph[0]):
                continue
            if graph[xx][yy] == 0 and visited[xx][yy][w] == 0:
                visited[xx][yy][w] = visited[x][y][w] + 1
                dq.append((xx, yy, w))
            elif graph[xx][yy] == 1 and w == 0:
                visited[xx][yy][w+1] = visited[x][y][w] + 1
                dq.append((xx, yy, w + 1))
    return -1
    
result = bfs()
print(result)