import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def dfs(x):
    res = 1
    for neib in graph[x]:
        if not visited[neib]:
            visited[neib] = True
            res += dfs(neib)
    return res
    

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())

    graph[b].append(a)

x = int(input())
visited = [False] * (n+1)

answer = 0
answer = dfs(x)
print(answer - 1)