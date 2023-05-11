import sys

from collections import defaultdict

input = sys.stdin.readline

def bellman_ford(graph, V):
    INF = 10**9
    distances = [INF for _ in range(V+1)]
    distances[1] = 0
    
    for i in range(V):
        for curr in range(1, V+1):
            for e, t in graph[curr]:
                if distances[e] > distances[curr] + t:
                    distances[e] = distances[curr] + t
                    if i == V-1: return True
    return False


T = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())
    
    graph = defaultdict(list)

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    
    if bellman_ford(graph, N):
        print("YES")
    else:
        print("NO")
