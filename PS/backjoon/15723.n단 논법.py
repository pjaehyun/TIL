import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(start, end):
    res = False

    if start == end:
        return True
    for neib in graph[start]:
        if neib not in visited:
            visited.add(neib)
            res |= dfs(neib, end)
    return res

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    a, _, b = map(str, input().split())
    graph[a].append(b)

m = int(input())

for _ in range(m):
    visited = set()
    start, _, end = map(str, input().split())
    visited.add(start)
    if dfs(start, end):
        print("T")
    else:
        print("F")