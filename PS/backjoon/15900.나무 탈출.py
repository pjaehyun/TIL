import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, step):
    if len(graph[x]) == 1 and visited[graph[x][0]]:
        leafs.append(step)
    for neib in graph[x]:
        if not visited[neib]:
            visited[neib] = True
            dfs(neib, step + 1)

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
visited[1] = True
leafs = []
dfs(1, 0)

if sum(leafs) % 2 == 0:
    print("No")
else:
    print("Yes")