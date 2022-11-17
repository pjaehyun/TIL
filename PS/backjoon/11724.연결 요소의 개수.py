import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
visited = set()
answer = 0

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(start, graph):
    dq = deque()
    dq.append(start)
    visited.add(start)

    while dq:
        node = dq.popleft()
        
        for e in graph[node]:
            if e not in visited:
                visited.add(e)
                dq.append(e)
 
# def dfs(start):
#     visited.add(start)
#     for e in graph[start]:
#         if e not in visited:
#             dfs(e)


for i in range(1, N+1):
    if i not in visited:
        answer += 1
        bfs(i, graph)
        # dfs(i)
    
    if len(visited) == N:
        print(answer)
        exit(0)
