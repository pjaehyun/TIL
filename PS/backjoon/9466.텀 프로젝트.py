import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

t = int(input())

def dfs(curr, cycle):
    global answer
    visited.add(curr)
    cycle.append(curr)

    if graph[curr] not in visited:
        dfs(graph[curr], cycle)
    else:
        if graph[curr] in cycle:
            answer -= len(cycle[cycle.index(graph[curr]):])

for _ in range(t):
    n = int(input())
    stu = list(map(int, input().split()))
    graph = defaultdict(int)
    visited = set()
    answer = n

    for i in range(n):
        graph[i+1] = stu[i]

    for i in range(1, n+1):
        if i not in visited:
            dfs(i, [])
    print(answer)