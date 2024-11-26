import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    dq = deque()
    dq.append((x, y, 0))
    visited[x][y] = True

    while dq:
        x, y, step = dq.popleft()
        if (x, y) == (n-1, m-1):
            return step

        for i in range(1, graph[x][y] + 1):
            if x+i<n and not visited[x+i][y]:
                visited[x+i][y] = True
                dq.append((x+i,y,step+1))
            
            if y+i<m and not visited[x][y+i]:
                visited[x][y+i] = True
                dq.append((x,y+i,step+1))
print(bfs(0, 0))