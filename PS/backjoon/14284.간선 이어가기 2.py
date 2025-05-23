import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

def dijkstra(s, e):
    distances = [float('inf')] * (n+1)

    hq = []
    
    distances[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        distance, curr = heapq.heappop(hq)
        for neib, weight in graph[curr]:
            if distances[neib] > distance + weight:
                distances[neib] = distance + weight
                heapq.heappush(hq, (distance + weight, neib))
    
    return distances[e]

print(dijkstra(s, t))