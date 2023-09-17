import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(list(map(int, input().split())))

def bs(num, n):
    l, r = 0, n-1
    
    while l < r:
        mid = (l+r) // 2

        if lis[mid] < num:
            l = mid + 1
        else:
            r = mid
    return l

lis = [arr.popleft()]
lis_idx = [(lis[0], 0)]

while arr:
    curr = arr.popleft()
    if lis[-1] < curr:
        lis.append(curr)
        lis_idx.append((curr, len(lis) - 1))
    else:
        idx = bs(curr, len(lis))
        lis[idx] = curr
        lis_idx.append((curr, idx))

answer = []
temp = len(lis) - 1
for i in range(len(lis_idx)-1, -1, -1):
    if temp == lis_idx[i][1]:
        answer.append(lis_idx[i][0])
        temp -= 1

print(len(answer))
for a in answer[::-1]:
    print(a, end = " ")