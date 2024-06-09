import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [input().strip() for _ in range(n)]

def bfs():
    dq = deque()
    distances = [[-1] * n for _ in range(n)]

    dq.append((0, 0))
    distances[0][0] = 0

    while dq:
        x, y = dq.popleft()

        if x == n-1 and y == n-1:
            return distances[x][y]
        
        for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<n and 0<=ny<n and distances[nx][ny] == -1:
                if graph[nx][ny] == '0':
                    dq.append((nx, ny))
                    distances[nx][ny] = distances[x][y] + 1
                else:
                    dq.appendleft((nx, ny))
                    distances[nx][ny] = distances[x][y]
                
print(bfs())