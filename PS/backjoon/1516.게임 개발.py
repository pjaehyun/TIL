import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

times = [0]
graph = defaultdict(list)
indegree = [0] * (n+1)

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    times.append(lst[0])
    for j in range(1, len(lst) - 1):
        graph[lst[j]].append(i)
        indegree[i] += 1

dq = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
answer = [0] * (n+1)
while dq:
    curr = dq.popleft()
    answer[curr] += times[curr]
    for neib in graph[curr]:
        indegree[neib] -= 1
        answer[neib] = max(answer[neib], answer[curr])
        if indegree[neib] == 0:
            dq.append(neib)

for i in range(1, n+1):
    print(answer[i])