import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
    p = deq.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        deq.rotate(-(p[1] - 1))
    else:
        deq.rotate(-p[1])
