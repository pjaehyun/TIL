import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dq = deque()

dq.append((0, 0))

visited = [False] * n
visited[0] = True
answer = -1

while dq:
    
    curr, jump = dq.popleft()
    if curr >= (n-1):
        answer = jump
        break

    for i in range(curr+1, curr + arr[curr]+1):
        if i < n and not visited[i]:
            visited[i] = True
            dq.append((i, jump+1))
print(answer)