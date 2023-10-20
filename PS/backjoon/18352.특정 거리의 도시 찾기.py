import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

INF = float('inf')

n, m, k, x = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (start, 0))
    distances = [INF] * (n+1)
    distances[start] = 0

    while hq:
        curr, dist = heapq.heappop(hq)

        for neib in graph[curr]:
            if dist + 1 < distances[neib]:
                distances[neib] = dist + 1
                heapq.heappush(hq, (neib, dist + 1))
    return distances

distances = dijkstra(x)

nothing = True
for i in range(len(distances)):
    if distances[i] == k:
        print(i)
        nothing = False
if nothing:
    print(-1)

