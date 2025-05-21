import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, d = map(int, input().split())
shortcut = defaultdict(list)

for _ in range(n):
    x, y, w = map(int, input().split())

    shortcut[x].append((y, w))


def dijkstra(x):
    distances = [float('inf')] * 10001

    hq = []

    heapq.heappush(hq, (0, x))
    distances[0] = 0

    while hq:
        distance, x = heapq.heappop(hq)

        for neib, weight in shortcut[x]:
            if distances[neib] > distance + weight:
                distances[neib] = distance + weight
                heapq.heappush(hq, (distance+weight, neib))
        if x < 10000:
            if distances[x+1] > distance + 1:
                distances[x+1] = distance + 1
                heapq.heappush(hq, (distance+1, x+1))
    return distances

res = dijkstra(0)

print(res[d])