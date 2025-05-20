import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    
    dq = deque()

    dq.append((x, y))
    footprint = [(x, y)]
    while dq:
        x, y = dq.popleft()

        for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
            if 0<=nx<12 and 0<=ny<6 and puyo[nx][ny] == puyo[x][y] and not visited[nx][ny]:
                footprint.append((nx, ny))
                visited[nx][ny] = True
                dq.append((nx, ny))
    
    if len(footprint) > 3:
        for x, y in footprint:
            puyo[x][y] = '.'
        return True
    return False

def down():

    for j in range(6):
        temp = []
        for i in range(11, -1, -1):
            if puyo[i][j] != '.':
                temp.append(puyo[i][j])
                puyo[i][j] = '.'
        idx = 11
        for e in temp:
            puyo[idx][j] = e
            idx -= 1
    
                
    

puyo = [list(input().strip()) for _ in range(12)]
answer = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    not_break = True
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                if bfs(i, j):
                    not_break = False
    if not_break:
        break
    answer += 1
    down()
print(answer)