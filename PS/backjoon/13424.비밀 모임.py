import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(x, rooms):
    distances = [float('inf')] * (n+1)
    
    hq = []

    heapq.heappush(hq, (0, x))
    distances[x] = 0

    while hq:
        distance, curr = heapq.heappop(hq)

        for neib, weight in graph[curr]:
            if distances[neib] > weight + distance:
                distances[neib] = weight + distance
                heapq.heappush(hq, (weight + distance, neib))
    
    for i in range(1, n+1):
        rooms[i-1] += distances[i]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    k = int(input())
    friends = list(map(int, input().split()))

    rooms = [0] * n

    for friend in friends:
        dijkstra(friend, rooms)
    
    min_distance = min(rooms)

    for i in range(n):
        if rooms[i] == min_distance:
            print(i+1)
            break