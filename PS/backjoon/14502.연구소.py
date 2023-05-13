import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0

def virus(graph, n, m):
    dq = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for xx, yy in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 0:
                graph[xx][yy] = 2
                dq.append((xx, yy))
    return count(graph, n, m)

def count(graph, n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                res += 1
    return res

def build(graph, n, m, count):
    global answer
    if count == 3: 
        temp = copy.deepcopy(graph)
        res = virus(temp, n,m)
        answer = max(answer, res)
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                build(graph, n, m, count+1)
                graph[i][j] = 0

build(graph, N, M, 0)
print(answer)
