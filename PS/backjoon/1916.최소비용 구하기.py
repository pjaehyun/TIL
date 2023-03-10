import sys, heapq

input = sys.stdin.readline

N, M = int(input()), int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances = [float('inf')] * (N+1)
    
    while q:
        distance, current = heapq.heappop(q)
        if distances[current] < distance:
            continue
        for nei in graph[current]:
            weight = nei[1] + distance
            if weight < distances[nei[0]]:
                distances[nei[0]] = weight
                heapq.heappush(q, (weight, nei[0]))
    return distances

start, end = map(int, input().split())

distances = dijkstra(start)
print(distances[end])