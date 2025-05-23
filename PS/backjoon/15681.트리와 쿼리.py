import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def make_tree(parent):
    for child in graph[parent]:
        if not visited[child]:
            tree[parent].append(child)
            visited[child] = True
            make_tree(child)

def dfs(x):
    res = 0
    for neib in tree[x]:
        res += 1 + dfs(neib)
        
    count[x] = res
    return res

n, r, q = map(int, input().split())

graph = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

tree = defaultdict(list)
visited = [False] * (n+1)

visited[r] = True
make_tree(r)

count = [0] * (n+1)

dfs(r)

for _ in range(q):
    u = int(input())
    print(count[u] + 1)
