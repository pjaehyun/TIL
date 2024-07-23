import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
indegree = [0] * (n + 1)
q = deque()
answer = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        answer[i] = 1

term = 2
while q:
    for _ in range(len(q)):
        curr = q.popleft()

        for neib in graph[curr]:
            indegree[neib] -= 1
            if indegree[neib] == 0:
                q.append(neib)
                answer[neib] = term
    term += 1
print(*answer[1:])