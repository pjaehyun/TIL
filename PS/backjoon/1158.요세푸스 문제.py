import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

arr = deque([x for x in range(1, n+1)])
answer = []

temp = 0
while arr:
    x = arr.popleft()
    temp += 1
    if temp == k:
        temp = 0
        answer.append(x)
    else: arr.append(x)
print("<", end="")
for i in range(n):
    if i == n-1:
        print(answer[i], end="")
    else:
        print(answer[i], end=", ")
print(">", end="")