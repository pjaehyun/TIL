import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    dq = deque()
    visited = [[False] * (w+2) for _ in range(h+2)]

    dq.append((x, y))
    visited[x][y] = True
    count = 0

    while dq:
        x, y = dq.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<h+2 and 0<=ny<w+2 and not visited[nx][ny]:
                if graph[nx][ny] == '.':
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                elif graph[nx][ny].islower():
                    door[ord(graph[nx][ny]) - ord('a')] = 1
                    dq = deque()
                    visited = [[False] * (w+2) for _ in range(h+2)]
                    graph[nx][ny] = '.'
                    dq.append((nx, ny))
                elif graph[nx][ny].isupper():
                    if door[ord(graph[nx][ny]) - ord('A')]:
                        visited[nx][ny] = True
                        graph[nx][ny] = '.'
                        dq.append((nx, ny))
                elif graph[nx][ny] == '$':
                    visited[nx][ny] = True
                    count += 1
                    graph[nx][ny] = '.'
                    dq.append((nx, ny))
    return count

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    keys = input().strip()
    door = [0] * 26

    for key in keys:
        if key != '0':
            door[ord(key) - ord('a')] = 1

    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(graph[i][j]) <= ord('Z'):
                if door[ord(graph[i][j]) - ord('A')]:
                    graph[i][j] = '.'

    for i in range(h):
        graph[i].insert(0, '.')
        graph[i].append('.')

    graph.insert(0, ['.' for _ in range(w+2)])
    graph.append(['.' for _ in range(w+2)])

    print(bfs(0, 0))