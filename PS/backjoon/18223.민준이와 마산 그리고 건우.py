import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

v, e, p = map(int, input().split())

graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(x):
    
    distances = [float('inf')] * (v+1)

    hq = []

    heapq.heappush(hq, (0, x))
    distances[x] = 0

    while hq:
        distance, curr = heapq.heappop(hq)

        for neib, weight in graph[curr]:
            if distances[neib] > weight + distance:
                distances[neib] = weight + distance
                heapq.heappush(hq, (weight + distance, neib))
    return distances

mj_res = dijkstra(1)

mj_to_ms = mj_res[-1]
mj_to_gw = mj_res[p]

gw_res = dijkstra(p)

gw_to_ms = gw_res[-1]

if mj_to_ms < gw_to_ms + mj_to_gw:
    print("GOOD BYE")
else:
    print("SAVE HIM")