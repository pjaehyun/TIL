# Disjoint Set(시간복잡도와 공간복잡도상 우위에 있음)
import sys

import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

UF = {x:x for x in range(1, N+1)}
hq = []


def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX > rootY:
        UF[rootX] = rootY
    else:
        UF[rootY] = rootX

def find(x):
    if x != UF[x]:
        UF[x] = find(UF[x])
    return UF[x]

for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(hq, (-C, A, B))

start, end = map(int, input().split())

answer = float('inf')
while hq:
    C, A, B = heapq.heappop(hq)
    union(A, B)
    answer = min(answer, -C)
    if find(start) == find(end):
        break
print(answer)
    

# BFS & Binary Search
import sys

from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

islands = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    islands[A].append((B,C))
    islands[B].append((A,C))

start, end = map(int, input().split())


def bfs(mid):
    dq = deque()
    dq.append(start)
    visited = set()
    visited.add(start)

    while dq:
        island = dq.popleft()
        for nei in islands[island]:
            if nei[0] not in visited and nei[1] >= mid:
                visited.add(nei[0])
                dq.append(nei[0])
    return True if end in visited else False

left, right = 1, 1000000000
answer = 1
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
