import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, r = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for k, v in graph.items():
    graph[k] = sorted(graph[k])

def dfs(x, depth):
    answer[x] = depth

    for neib in graph[x]:
        if answer[neib] == -1:
            dfs(neib, depth+1)

answer = {x:-1 for x in range(1, n+1)}

answer[r] = 0
dfs(r, 0)

for k, v in answer.items():
    print(v)