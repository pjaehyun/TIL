import sys
from collections import defaultdict, deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prev = list(map(int, input().split()))
    m = int(input())

    graph = defaultdict(list)
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[prev[i]].append(prev[j])
            indegree[prev[j]] += 1

    for _ in range(m):
        a, b = map(int, input().split())
        flag = True

        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
            flag = False
        
        if flag:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
    
    
    dq = deque()
    answer = []
    
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            dq.append(i)
    
    while dq:
        curr = dq.popleft()
        answer.append(curr)
        for neib in graph[curr]:
            indegree[neib] -= 1
            if indegree[neib] == 0:
                dq.append(neib)
    
    if len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(*answer)