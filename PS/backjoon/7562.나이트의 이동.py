import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, x1, y1, x2, y2):
    visited = [[False] * n for _ in range(n)]
    visited[x1][y1] = True
    dq = deque([(x1, y1, 0)])

    while dq:
        x, y, step = dq.popleft()
        if (x, y) == (x2, y2):
            return step

        for dx, dy in [(x-1, y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2)]:
            if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
                dq.append((dx, dy, step+1))
                visited[dx][dy] = True
    return 0


t = int(input())

for _ in range(t):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    print(bfs(n, x1, y1, x2, y2))
