# Pypy3로 제출
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(n):
    dq = deque()
    dq.append((n, ''))
    visited[n] = True

    while dq:
        a, c = dq.popleft()
        if a == B:
            return c

        D = a * 2
        if D > 9999:
            D = D % 10000

        S = a - 1
        if a == 0:
            S = 9999

        L = (a % 1000)*10 + (a // 1000)
        R = (a % 10)*1000 + (a // 10)


        for aa, command in [(D, 'D'), (S, 'S'), (L, 'L'), (R, 'R')]:
            if not visited[aa]:
                dq.append((aa, c+command))
                visited[aa] = True


for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10001
    print(bfs(A))

