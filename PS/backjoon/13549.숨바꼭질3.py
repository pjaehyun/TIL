# 첫번째 풀이(BFS)
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dq = deque()
visited = [False] * 100001
dq.append((N, 0))
visited[N] = True

while dq:
    curr, second = dq.popleft()

    if curr == K:
        print(second)
        break

    if curr*2 <= 100000 and not visited[curr*2]:
        dq.append((curr * 2, second))
        visited[curr*2] = True
    if curr-1 >= 0 and not visited[curr-1]:
        dq.append((curr - 1, second + 1))
        visited[curr-1] = True
    if curr+1 <= 100000 and not visited[curr+1]:
        dq.append((curr + 1, second + 1))
        visited[curr+1] = True

# 두번째 풀이(다익스트라)
import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

graph = [[] for _ in range(100001)]

for i in range(100001):
    if i * 2 < 100001:
        graph[i].append([i*2, 0])
    if i - 1 >= 0:
        graph[i].append([i-1, 1])
    if i + 1 < 100001:
        graph[i].append([i+1, 1])

def dijkstra(start, end, graph):
    hq = []

    distances = [float('inf')] * 100001
    visited = [False] * 100001

    heapq.heappush(hq, (0, start))
    visited[start] = True
    distances[start] = 0
    
    while hq:
        distance, node = heapq.heappop(hq)
        for neib, weight in graph[node]:
            if not visited[neib] and distances[neib] > distance + weight:
                distances[neib] = distance + weight
                heapq.heappush(hq, (distances[neib], neib))
    return distances[end]
print(dijkstra(N, K, graph))