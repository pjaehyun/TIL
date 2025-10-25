import sys
from collections import defaultdict, deque
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[float('inf')] * (v+1) for _ in range(v+1)]


for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = float('inf')

for i in range(1, v+1):
    answer = min(answer, graph[i][i])

if answer == float('inf'): print(-1)
else: print(answer)
