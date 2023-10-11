import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

dq = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)

answer = []
while dq:
    curr = dq.popleft()
    answer.append(curr)

    for neib in graph[curr]:
        indegree[neib] -= 1
        if indegree[neib] == 0:
            dq.append(neib)

for a in answer:
    print(a, end=" ")
