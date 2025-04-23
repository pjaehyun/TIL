import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dq = deque()
answer = 0

for i in range(n):
    info = list(map(int, input().split()))

    if info[0] == 1:
        if not dq:
            dq.append(info + [1])
        else:
            if info[2] == 1: answer += info[1]
            else: dq.appendleft(info + [1])
    else:
        if dq:
            dq[0][3] += 1
            if dq[0][2] - dq[0][3] <= 0:
                temp = dq.popleft()
                answer += temp[1]
print(answer)