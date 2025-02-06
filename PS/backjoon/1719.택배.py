import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, w))
    graph[b-1].append((a-1, w))

def dijkstra(start):
    
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0

    hq = []
    heapq.heappush(hq, (0, start, []))
    route = [[] for _ in range(n)]
    while hq:
        dist, curr, temp = heapq.heappop(hq)
        for neib, weight in graph[curr]:
            if dist + weight < distances[neib]:
                distances[neib] = dist + weight
                heapq.heappush(hq, (dist + weight, neib, temp + [neib]))
                route[neib] = temp + [neib]
    
    for r in route:
        if r:
            print(r[0]+1, end=" ")
        else: print('-', end=" ")
    

for i in range(n):
    dijkstra(i)
    print()