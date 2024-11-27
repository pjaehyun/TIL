import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(p, g):
    if visited[graph[p]] == 0:
        visited[graph[p]] = g
        dfs(graph[p], g)

idx = 1
while True:
    n = int(input())
    if n == 0:
        break

    graph = defaultdict(str)
    visited = {}
    for _ in range(n):
        a, b = map(str, input().strip().split())
        graph[a] = b
        visited[a] = 0
        visited[b] = 0
    
    group = 1
    for part in visited.keys():
        if visited[part] == 0:
            visited[part] = group
            dfs(part, group)
            group += 1
    
    print(idx, len(set(visited.values())))
    
    idx += 1