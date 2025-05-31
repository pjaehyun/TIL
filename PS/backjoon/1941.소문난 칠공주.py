import sys
from collections import deque
input = sys.stdin.readline

graph = [input().strip() for _ in range(5)]
answer = 0

def bfs():
    
    visited = [[True] * 5 for _ in range(5)]
    
    for x, y in arr:
        visited[x][y] = False
    
    dq = deque()
    dq.append(arr[0])
    visited[arr[0][0]][arr[0][1]] = True
    
    s_count = 1 if graph[arr[0][0]][arr[0][1]] == "S" else 0
    count = 1

    while dq:
        x, y = dq.popleft()
        for nx, ny in [(x+1,y), (x,y+1),(x,y-1),(x-1,y)]:
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
                if graph[nx][ny] == "S": s_count += 1
                count += 1
    if count >= 7 and s_count >= 4:
        return True
    return False

def dfs(start, count):
    global answer
    if count == 7:
        if bfs():
            answer += 1
        return
    for i in range(start, 25):
        r, c = i // 5, i % 5
        arr.append((r, c))
        dfs(i + 1, count + 1)
        arr.pop()

arr = []

dfs(0, 0)
print(answer)