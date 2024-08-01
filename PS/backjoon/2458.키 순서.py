#Pypy3로 제출
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(n):
    check = True
    for j in range(n):
        if graph[i][j] == float('inf') and graph[j][i] == float('inf'):
            check = False
            break
    if check:
        answer += 1
print(answer)