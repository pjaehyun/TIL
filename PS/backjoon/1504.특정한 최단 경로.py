import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

def dijkstra(start, end):
    if start == end:
        return 0
    hq = []
    heapq.heappush(hq, (0, start))

    distances = [float('inf') for _ in range(N+1)]
    
    while hq:
        dist, curr = heapq.heappop(hq)
        
        for nei, weight in graph[curr]:
            if dist + weight < distances[nei]:
                distances[nei] = dist + weight
                heapq.heappush(hq, (dist+weight, nei))
    return distances[end]

v1, v2 = map(int, input().split())

first = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
second = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

answer = min(first, second)

if answer == float('inf'):
    print(-1)
else:
    print(answer)