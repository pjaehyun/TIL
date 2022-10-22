import heapq
N, M, X = map(int, input().split())

student = [[] for _ in range(N+1)]
shortest_distances = [0 for _ in range(N+1)]
result = 0

for _ in range(M):
    start, end, time = map(int, input().split())
    student[start].append((end, time))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0

    while q:
        distance, now = heapq.heappop(q)
        if distances[now] < distance:
            continue
        for i in student[now]:
            weight = distance + i[1]
            if weight < distances[i[0]]:
                distances[i[0]] = weight
                heapq.heappush(q, (weight, i[0]))
    return distances

for i in range(1, N+1):
    shortest_distances[i] = dijkstra(i)

for i in range(1, N+1):
    if i == X:
        continue
    result = max(result, shortest_distances[i][X] + shortest_distances[X][i])
print(result)