import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())

def topology(indegree, graph, times, n):
    distances = [0] * (n+1)
    dq = deque()
    
    start = [i for i in range(1, len(indegree)) if indegree[i] == 0]

    for e in start:
        dq.append(e)
        distances[e] = times[e]
    
    while dq:
        curr = dq.popleft()
        for neib in graph[curr]:
            indegree[neib] -= 1
            distances[neib] = max(distances[neib], distances[curr] + times[neib])
            if indegree[neib] == 0:
                dq.append(neib)
    return distances
    

def solve():
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    graph = defaultdict(list)
    indegree = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    end = int(input())
    distances = topology(indegree, graph, [0] + times, n)
    print(distances[end])
for _ in range(T):
    solve()