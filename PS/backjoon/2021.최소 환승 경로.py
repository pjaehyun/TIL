from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(start, end, subways):
    if start == end:
        return 0
    visited_subway = [False for _ in range(len(subways))]
    visited_station = [False for _ in range(N + 1)]

    dq = deque()
    for subway in graph[start]:
        dq.append((subway, 0))
        visited_subway[subway] = True
    visited_station[start] = True
    
    while dq:
        subway, count = dq.popleft()
        for station in subways[subway]:
            if visited_station[station]:
                continue
            if station == end:
                return count            
            visited_station[station] = True
            for trans in graph[station]:
                if not visited_subway[trans]:
                    dq.append((trans, count+1))
                    visited_subway[trans] = True
    return -1
            
N, L = map(int, input().split())

graph = defaultdict(list)
subways = []
for i in range(L):
    lst = list(map(int, input().split()))
    subways.append(lst[:-1])
    for l in lst:
        if l == -1:
            continue
        graph[l].append(i)

start, end = map(int, input().split())
result = bfs(start, end, subways)
print(result)