import sys, heapq

input = sys.stdin.readline

def dijkstra(graph, start, n):
    routes = [[float('inf'), 0] for _ in range(n+1)]
    hq = []
    heapq.heappush(hq, (start, 0))
    while hq:
        current, distance = heapq.heappop(hq)
        if routes[current][0] < distance:
            continue

        for neib in graph[current]:
            weight = neib[1] + distance
            if weight < routes[neib[0]][0]:
                routes[neib[0]][0] = weight
                routes[neib[0]][1] = current
                heapq.heappush(hq, (neib[0], weight))
    return routes

n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
start, end = map(int, input().split())

routes = dijkstra(graph, start, end, n)

print(routes[end][0])

curr = end
path = [end]
while curr != start:
    curr = routes[curr][1]
    path.append(curr)

print(len(path))
for p in path[::-1]:
    print(p, end=" ")