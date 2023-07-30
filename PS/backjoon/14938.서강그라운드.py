# 풀이방식1(워셜 프롤이드)
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a][b] = d
    graph[b][a] = d

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            temp += items[j-1]
    answer = max(answer, temp)
print(answer)

# 풀이방식2(다익스트라)
import sys, heapq
from collections import defaultdict, deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(r):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def dijkstra(node):
    distances = [float('inf')] * (n + 1)

    hq = []
    heapq.heappush(hq, (0, node))
    distances[node] = 0
    while hq:
        dist, curr = heapq.heappop(hq)
        for neib, weight in graph[curr]:
            if dist + weight <= distances[neib]:
                heapq.heappush(hq, (dist+weight, neib))
                distances[neib] = dist + weight
    res = 0
    for i in range(1, n+1):
        if distances[i] <= m:
            res += items[i-1]
    return res



answer = 0
for i in range(1, n+1):
    answer = max(answer, dijkstra(i))
print(answer)