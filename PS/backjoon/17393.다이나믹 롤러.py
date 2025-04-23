import sys
input = sys.stdin.readline

def bs(l, r, x):
    while l <= r:
        mid = (l + r) // 2

        if x >= b[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
for i in range(n):
    idx = bs(0, n-1, a[i])
    answer.append(idx - i - 1)
print(*answer)