import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

s, xx, yy = map(int, input().split())


start = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            start.append((graph[i][j], i, j))
start.sort()

dq = deque(start)
time = 0
while dq:
    if time == s:
        break

    for _ in range(len(dq)):
        virus, x, y = dq.popleft()
        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = virus
                dq.append((virus, nx, ny))
    time += 1
print(graph[xx-1][yy-1])