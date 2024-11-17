import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def bfs(x):
    dq = deque()
    dq.append((x, 0, [x]))
    
    visited = set()
    visited.add(x)
    while dq:
        num, step, foot_print = dq.popleft()
        if num == 1:
            return step, foot_print
        if num % 3 == 0 and num//3 not in visited:
            visited.add(num//3)
            dq.append((num//3, step+1, foot_print+[num//3]))
        if num % 2 == 0 and num//2 not in visited:
            visited.add(num//2)
            dq.append((num//2, step+1, foot_print+[num//2]))
        
        if num-1 not in visited:
            visited.add(num-1)
            dq.append((num-1, step+1, foot_print+[num-1]))
    return None
step, foot_print = bfs(n)
print(step)
print(*foot_print)