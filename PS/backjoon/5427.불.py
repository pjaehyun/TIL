import sys
import copy
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(w, h, graph):
    dq = deque()
    start = None
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                dq.append((i, j, graph[i][j]))
            elif graph[i][j] == "@":
                start = (i, j, graph[i][j])

    dq.append(start)

    time = 0

    while dq:
        for _ in range(len(dq)):
            x, y, curr = dq.popleft()
            
            for nx, ny in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    if curr == "@":
                        return time + 1
                if 0<=nx<h and 0<=ny<w and graph[nx][ny] == ".":
                    graph[nx][ny] = curr
                    dq.append((nx, ny, graph[nx][ny]))
        time += 1

    return "IMPOSSIBLE"

t = int(input())

for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    
    print(bfs(w, h, graph))