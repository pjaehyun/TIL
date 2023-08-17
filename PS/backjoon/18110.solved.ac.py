import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

opinions = deque()
for _ in range(n):
    opinions.append(int(input()))

opinions = deque(sorted(opinions))

tm = round(n*0.15+0.0000001)

for _ in range(tm):
    if opinions:
        opinions.popleft()
    if opinions:
        opinions.pop()
if opinions:
    print(round((sum(opinions) / len(opinions)) + 0.0000001))
else:
    print(0)