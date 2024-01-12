import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

answer = False
graph = defaultdict(list)
visited = set()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bt(node, level):
    global answer

    if level >= 5:
        answer = True
        return
    for neib in graph[node]:
        if neib not in visited:
            visited.add(neib)
            bt(neib, level+1)
            visited.remove(neib)

for i in range(n):
    visited.add(i)
    bt(i, 1)
    visited.remove(i)
    if answer:
        break;

if answer:
    print(1)
else:
    print(0)