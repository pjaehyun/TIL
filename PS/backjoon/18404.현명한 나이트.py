import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dq = deque()

    dq.append((x, y, 0))
    
    while dq:
        x, y, step = dq.popleft()
        if (x, y) in dest:
            answer[dest[(x, y)]] = step
        for nx, ny in [(x-2,y-1), (x-2,y+1), (x-1,y-2), (x-1,y+2), (x+1,y-2), (x+1,y+2), (x+2,y-1), (x+2,y+1)]:
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny, step+1))
    return 0

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

x, y = map(int, input().split())

visited = [[False] * n for _ in range(n)]

answer = [0] * m

dest = {}

for i in range(m):
    a, b = map(int, input().split())
    dest[(a-1, b-1)] = i

bfs(x-1, y-1)
visited[x-1][y-1] = True
print(*answer)