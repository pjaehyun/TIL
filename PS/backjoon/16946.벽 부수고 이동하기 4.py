import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[int(x) for x in list(input().strip())] for _ in range(n)]
area = [[0 if graph[i][j] == 0 else -1 for j in range(m)] for i in range(n)]
area_count = {}
def bfs_idx(i, j, idx, res):
    dq = deque()
    dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for xx, yy in [[x, y+1],[x+1, y],[x, y-1],[x-1, y]]:
            if 0 <= xx < n and 0 <= yy < m and area[xx][yy] == 0:
                area[xx][yy] = idx
                res += 1
                dq.append((xx, yy))
    return res

idx = 1
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            area[i][j] = idx
            area_count[idx] = bfs_idx(i, j, idx, 1)
            idx += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited = set()
            for ii, jj in [[i, j+1],[i+1, j],[i, j-1],[i-1, j]]:
                if 0 <= ii < n and 0 <= jj < m and graph[ii][jj] == 0 and area[ii][jj] not in visited:
                    graph[i][j] += area_count[area[ii][jj]]
                    visited.add(area[ii][jj])

for i in range(n):
    for j in range(m):
        print(graph[i][j] % 10, end="")
    print()