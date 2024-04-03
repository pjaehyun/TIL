import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(x):
    if graph[x] not in visited:
        visited.add(graph[x])
        dfs(graph[x])

t = int(input())

for _ in range(t):
    n = int(input())
    perm = list(map(int, input().split()))
    graph = defaultdict(int)
    visited = set()
    answer = 0

    for i in range(1, n+1):
        graph[i] = perm[i-1]
    
    for i in range(1, n+1):
        if i not in visited:
            visited.add(i)
            dfs(i)
            answer += 1
    print(answer)