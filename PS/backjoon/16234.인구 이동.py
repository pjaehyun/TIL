import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    
    dq = deque()
    dq.append((x, y))
    
    count = 1
    people_sum = arr[x][y]
    
    foot_print = [(x, y)]    

    while dq:
        x, y = dq.popleft()

        for nx, ny in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                count += 1
                people_sum += arr[nx][ny]
                dq.append((nx, ny))
                foot_print.append((nx, ny))
                visited[nx][ny] = True
    
    pop = people_sum // count

    if len(foot_print) > 1:
        for x, y in foot_print:
            arr[x][y] = pop
        return True
    return False


n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

days = 0

while True:
    visited = [[False] * n for _ in range(n)]

    move = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                move |= bfs(i, j)
    if not move:
        break
    days += 1
print(days)
        