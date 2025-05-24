import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

x1, y1, x2, y2 = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]

def bfs(x, y, end):

    hq = []

    hq.append((0, x, y))

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    while hq:

        step, x, y = heapq.heappop(hq)
        if (x, y) == end:
            return step
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == "0":
                    heapq.heappush(hq,(step, nx, ny))
                else:
                    heapq.heappush(hq,(step+1, nx, ny))
                visited[nx][ny] = True
    return -1
print(bfs(x1-1, y1-1, (x2-1,y2-1)))