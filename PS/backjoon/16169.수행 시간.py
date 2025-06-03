import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
indegree = [0] * n
nodes = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
times = [0] * n

for i in range(n):
    if nodes[i][0] == 1:
        dq.append(i)
        times[i] = nodes[i][1]
    for j in range(n):
        if i == j: continue
        if nodes[i][0]+1 == nodes[j][0]:
            graph[i].append(j)
            indegree[j] += 1

while dq:
    for _ in range(len(dq)):
        curr = dq.popleft()
        for neib in graph[curr]:
            indegree[neib] -= 1

            if indegree[neib] == 0:
                dq.append(neib)
            times[neib] = max(times[neib], times[curr] + (curr - neib)**2 + nodes[neib][1])
print(max(times))