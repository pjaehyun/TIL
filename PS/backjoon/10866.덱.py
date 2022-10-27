import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push_front':
        dq.appendleft(command[1])
    if command[0] == 'push_back':
        dq.append(command[1])
    if command[0] == 'pop_front':
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    if command[0] == 'pop_back':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    if command[0] == 'size':
        print(len(dq))
    if command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    if command[0] == 'back':
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)