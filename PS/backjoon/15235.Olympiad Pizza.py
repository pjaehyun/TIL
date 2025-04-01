import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = deque(list(enumerate(map(int, input().split()))))

answer = [0] * n

time = 1

while arr:
    i, c =  arr.popleft()
    c -= 1

    if c <= 0:
        answer[i] = time
    else:
        arr.append((i, c))
    time += 1
print(*answer)