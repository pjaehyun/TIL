import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.uf = {x:x for x in range(n)}

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry: return False

        if rx < ry:
            self.uf[ry] = rx
        else:
            self.uf[rx] = ry
        return True

def dijkstra(x):
    distances = [float('inf')] * n

    hq = []

    heapq.heappush(hq, (0, x))
    distances[x] = 0

    while hq:
        distance, curr = heapq.heappop(hq)
        distance = -distance
        for neib, weight in d_graph[curr]:
            if distances[neib] > weight + distance:
                distances[neib] = weight + distance
                heapq.heappush(hq, (-(weight+distance), neib))
    return max(distances)

n, k = map(int, input().split())

graph = []
d_graph = defaultdict(list)
for _ in range(k):
    a, b, c = map(int, input().split())

    graph.append([a, b, c])

min_graph = sorted(graph, key=lambda x:x[2])

min_uf = UnionFind(n)

min_cost = 0
for a, b, c in min_graph:
    if min_uf.union(a, b):
        min_cost += c
        d_graph[a].append((b, c))
        d_graph[b].append((a, c))
max_weight = 0
for i in range(n):
    if len(d_graph[i]) == 1:
        max_weight = max(max_weight, dijkstra(i))
    
print(min_cost)
print(max_weight)