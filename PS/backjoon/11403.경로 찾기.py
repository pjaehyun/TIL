from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

graph = [[x if x == 1 else float('inf') for x in list(map(int, input().split()))] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == float('inf'):
            graph[i][j] = '0'
        else:
            graph[i][j] = '1'

for g in graph:
    print(' '.join(g))