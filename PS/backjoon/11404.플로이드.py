N = int(input())
M = int(input())

distance = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    start, end, dist = map(int, input().split())
    distance[start-1][end-1] = min(distance[start-1][end-1], dist)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                distance[i][j] = 0
            else: distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
for i in range(N):
    for j in range(N):
        if distance[i][j] == float('inf'):
            distance[i][j] = 0
        print(distance[i][j], end=' ')
    print()
