import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n+1)

for _ in range(m):
    lst = list(map(int, input().split()))
    for i in range(2, len(lst)):
        graph[lst[i-1]].append(lst[i])
        indegree[lst[i]] += 1

dq = deque()
for i in range(1, len(indegree)):
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
if len(answer) == n:
    for a in answer:
        print(a)
else:
    print(0)