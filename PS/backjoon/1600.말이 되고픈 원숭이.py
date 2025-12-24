import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

k = int(input())

w, h = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(h)]

dq = deque()
visited = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

dq.append((0, 0, 0))
visited[0][0][0] = 0

answer = -1

while dq:
    x, y, step = dq.popleft()

    if (x, y) == (h-1, w-1):
        answer = visited[x][y][step]
        break

    for nx, ny in [(x-2,y+1),(x-1,y+2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),(x-1,y-2),(x-2,y-1)]:
        if step < k and 0<=nx<h and 0<=ny<w and not arr[nx][ny] and visited[nx][ny][step+1] == -1:
            dq.append((nx, ny, step+1))
            visited[nx][ny][step+1] = visited[x][y][step] + 1
    
    for nx, ny in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
        if 0<=nx<h and 0<=ny<w and not arr[nx][ny] and visited[nx][ny][step] == -1:
            dq.append((nx, ny, step))
            visited[nx][ny][step] = visited[x][y][step] + 1
            
print(answer)