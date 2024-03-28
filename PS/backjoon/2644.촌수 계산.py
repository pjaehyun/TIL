import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = -1
visited = set()
def bfs(start, end):
    dq = deque()

    dq.append((start, 0))

    visited.add(start)

    while dq:
        curr, dist = dq.popleft()
        if curr == end:
            return dist

        for neib in graph[curr]:
            if neib not in visited:
                visited.add(neib)
                dq.append((neib, dist+1))
    return -1

print(bfs(a, b))