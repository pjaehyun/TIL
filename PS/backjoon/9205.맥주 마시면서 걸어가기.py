import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    
    dq = deque()
    visited = [False] * n
    for i in range(n):
        x, y = stores[i]
        if abs(start[0] - x) + abs(start[1] - y) <= 1000:
            visited[i] = True
            dq.append((x, y))
    
    answer = False
    if abs(start[0] - end[0]) + abs(start[1] - end[1]) <= 1000:
        answer = True
    while dq:
        x, y = dq.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            answer = True
            break
        
        for i in range(n):
            x2, y2 = stores[i]
            if abs(x - x2) + abs(y - y2) <= 1000 and not visited[i]:
                dq.append((x2, y2))
                visited[i] = True
    
    if answer:
        print("happy")
    else:
        print("sad")