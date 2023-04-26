import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

for i in range(N-1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def dfs(node):
    for neib, dist in tree[node]:
        if visited[neib] == -1:
            visited[neib] = visited[node] + dist
            dfs(neib)

visited = [-1] * (N+1)
visited[1] = 0
dfs(1)

start = visited.index(max(visited))

visited = [-1] * (N+1)
visited[start] = 0
dfs(start)
print(max(visited))