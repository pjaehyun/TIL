import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

limits = deque([list(map(int, input().split())) for _ in range(n)])

yj = deque([list(map(int, input().split())) for _ in range(m)])

answer = 0

while limits and yj:
    l = limits.popleft()
    y = yj.popleft()
    if l[0] > y[0]:
        limits.appendleft([l[0] - y[0], l[1]])
    elif y[0] > l[0]:
        yj.appendleft([y[0] - l[0], y[1]])

    answer = max(answer, y[1] - l[1])
print(answer)