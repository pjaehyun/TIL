import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(x):
    dq = deque()
    dq.append((x, 0))

    while dq:
        curr, step = dq.popleft()
        barns.append((step, curr))
        for neib in graph[curr]:
            if not visited[neib]:
                visited[neib] = True
                dq.append((neib, step+1))

    

n, m = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (n+1)
barns = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
bfs(1)
barns.sort(reverse=True)
res, dist, count = -1, barns[0][0], 0

for barn in barns:
    if dist == barn[0]:
        res = barn[1]
        count += 1
    else:
        break
print(res, dist, count)