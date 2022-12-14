import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dist = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    s, e = map(int, input().split())
    dist[s-1][e-1] = 1
    dist[e-1][s-1] = 1

# 워셜 플로이드 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

answer = [float('inf'), 0]

for i in range(len(dist)):
    _sum = sum(dist[i])
    if _sum < answer[0]:
        answer[0] = _sum
        answer[1] = i+1
print(answer[1])