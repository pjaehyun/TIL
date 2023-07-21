# dp로 풀었으나 시간초과 
from collections import deque
n = int(input())

arr = list(map(int, input().split()))
dq = deque(arr)
answer = []

def bs(l, r, num):

    while l < r:
        mid = (l + r) // 2
        if answer[mid] < num:
            l = mid + 1
        else:
            r = mid
    return l

answer.append(dq.popleft())
while dq:
    num = dq.popleft()

    if num > answer[-1]:
        answer.append(num)
    else:
        i = bs(0, len(answer) - 1, num)
        answer[i] = num
print(len(answer))