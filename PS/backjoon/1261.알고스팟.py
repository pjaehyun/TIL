import sys
from collections import deque
import heapq

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(input().strip()))

hq = []
heapq.heappush(hq, (0, 0, 0))
while hq:
    count, x, y = heapq.heappop(hq)
    if x == N-1 and y == M-1:
        print(count)

    for xx, yy in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
        if 0 <= xx < N and 0 <= yy < M and graph[xx][yy] != "-1":
            if graph[xx][yy] == '1':
                heapq.heappush(hq, (count + 1, xx, yy))
            else:
                heapq.heappush(hq, (count, xx, yy))
            graph[xx][yy] = "-1"