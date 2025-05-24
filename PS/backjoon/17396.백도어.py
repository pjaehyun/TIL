import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

sight = list(map(int, input().split()))
sight[n-1] = 0

graph = defaultdict(list)

for _ in range(m):
    a, b, t = map(int, input().split())

    if sight[a] == 1 or sight[b] == 1:
        continue
    graph[a].append((b,t))
    graph[b].append((a,t))


def dijkstra(x):

    hq = []
    distances = [float('inf')] * n

    heapq.heappush(hq, (0, x))
    distances[x] = 0

    while hq:
        distance, curr = heapq.heappop(hq)
        if distances[curr] < distance: continue
        for neib, weight in graph[curr]:
            if distance + weight < distances[neib]:
                distances[neib] = distance + weight
                heapq.heappush(hq, (distance + weight, neib))
    return distances[n-1] if distances[n-1] != float('inf') else -1
print(dijkstra(0))