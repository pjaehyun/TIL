import sys
from collections import deque

input = sys.stdin.readline

R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

def diffusion(n, m):
    dq = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dq.append((graph[i][j], i, j))
    while dq:
        v, x, y = dq.popleft()
        count = 0
        d = v // 5
                
        for dx, dy in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] != -1:
                count += 1
                graph[dx][dy] += d
        graph[x][y] = graph[x][y] - (d * count)

def clean_up(x, y, n, m):
    end = x
    curr = 0
    # 오른쪽으로 이동
    while y < m-1:
        y += 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp

    # 위로 이동
    while x > 0:
        x -= 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    
    # 왼쪽으로 이동
    while y > 0:
        y -= 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    
    # 아래로 이동
    while x < end - 1:
        x += 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp

def clean_down(x, y, n, m):
    end = x
    curr = 0
    # 오른쪽으로 이동
    while y < m-1:
        y += 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    # 아래로 이동
    while x < n-1:
        x += 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    
    # 왼쪽으로 이동
    while y > 0:
        y -= 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    
    # 위로 이동
    while x > end + 1:
        x -= 1
        temp = graph[x][y]
        graph[x][y] = curr
        curr = temp
    

for _ in range(T):
    diffusion(R, C)
    x = 0
    while x < R:
        if graph[x][0] == -1:
            clean_up(x, 0, R, C)
            clean_down(x+1, 0, R, C)            
            x += 2
        else:
            x += 1
ans = 0
for g in graph:
    ans += sum(g)
print(ans + 2)