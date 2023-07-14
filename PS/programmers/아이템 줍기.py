from collections import deque
def check(rectangle, x, y):
    for r in rectangle:
        if r[0]*2 < x < r[2]*2 and r[1]*2 < y < r[3]*2:
            return False
    return True

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * (102) for _ in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)
        
        for yy in range(y1, y2+1):
            if check(rectangle, x1, yy): graph[yy][x1] = 1
            if check(rectangle, x2, yy): graph[yy][x2] = 1
        
        for xx in range(x1, x2+1):
            if check(rectangle, xx, y1): graph[y1][xx] = 1
            if check(rectangle, xx, y2): graph[y2][xx] = 1
    dq = deque()
    dq.append((characterY*2, characterX*2, 0))
    visited = [[False] * 102 for _ in range(102)]
    while dq:
        y, x, dist = dq.popleft()
        if x == itemX*2 and y == itemY*2:
            return dist // 2
        for dx, dy in [[x+1, y],[x, y+1],[x-1, y],[x, y-1]]:
            if graph[dy][dx] == 1 and not visited[dy][dx]:
                dq.append((dy, dx, dist + 1))
                visited[dy][dx] = True