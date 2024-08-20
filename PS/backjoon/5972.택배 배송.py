import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(s, e):
    distances = [float('inf') for _ in range(n+1)]
    
    hq = []
    heapq.heappush(hq, (0, s))

    while hq:
        distance, curr = heapq.heappop(hq)
        
        for neib, weight in graph[curr]:
            if distance + weight < distances[neib]:
                distances[neib] = distance + weight
                heapq.heappush(hq, (distance + weight, neib))
    print(distances[e])
dijkstra(1, n)
