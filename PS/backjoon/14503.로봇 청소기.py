import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
direction = [[-1,0],[0, 1],[1, 0],[0, -1]]

graph = [list(map(int, input().split())) for _ in range(n)]

def no_clean(x, y):
    for nx, ny in [(x-1, y),(x, y+1),(x+1, y),(x, y-1)]:
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            return True
    return False

def move(x, y, d):
    for i in range(4):
        d = (d + 3) % 4
        nx, ny = x+direction[d][0], y+direction[d][1]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
            return nx, ny, d
    return x, y, d

def reverse(x, y, d):
    if d == 0: return x+1, y
    if d == 1: return x, y-1
    if d == 2: return x-1, y
    if d == 3: return x, y+1
    
answer = 0
while True:
    if graph[x][y] == 0: 
        graph[x][y] = -1
        answer += 1

    if no_clean(x, y):
        x, y, d = move(x, y, d)
    else:
        x, y = reverse(x, y, d)
        if x < 0 or x > n-1 or y < 0 or y > m-1 or graph[x][y] == 1:
            break
print(answer)