import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, n, m):
    dq = deque()
    visited = [[False] * m for _ in range(n)]

    dq.append((i, j, 0))
    visited[i][j] = True

    res = 0

    while dq:
        for _ in range(len(dq)):
            x, y, step = dq.popleft()
            res = max(res, step)
            for nx, ny in [[x+1,y], [x,y+1], [x-1,y], [x,y-1]]:
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and world[nx][ny] == "L":
                    dq.append((nx, ny, step+1))
                    visited[nx][ny] = True
    return res
                


n, m = map(int, input().split())

world = [list(input().strip()) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if world[i][j] == 'L':
            answer = max(answer, bfs(i, j, n, m))
print(answer)