import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

t = int(input())

def dijkstra(n, start, graph):
    distances = [float('inf') * (n+1) for _ in range(n+1)]

    hq = []
    distances[start] = 0
    heapq.heappush(hq, (start, 0))
    while hq:
        curr, distance = heapq.heappop(hq)
        for neib, weight in graph[curr]:
            if distances[neib] > distance + weight:
                distances[neib] = distance + weight
                heapq.heappush(hq, (neib, distance + weight))
    res = [distances[i] for i in range(len(distances)) if distances[i] != float("inf")]    
    return len(res), max(res)


for _ in range(t):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    count, time = dijkstra(n, c, graph)
    print(count, time)
