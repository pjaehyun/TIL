import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, t):
    dq = deque()

    dq.append((s, t, 0))

    while dq:
        s, t, step = dq.popleft()
        if s == t:
            return step
        if s < t:
            for ns, nt in [(s + s, t + 3), (s+1, t)]:
                dq.append((ns, nt, step + 1))
    return 0

    

c = int(input())

for _ in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t))