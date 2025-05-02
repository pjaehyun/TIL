import sys
input = sys.stdin.readline

def bs_right(l, r, x):
    while l <= r:
        mid = (l + r) // 2

        if x >= arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l

def bs_right2(l, r, x):
    while l < r:
        mid = (l + r) // 2

        if x >= (3*mid)*(mid-1)+1:
            l = mid + 1
        else:
            r = mid
    return l - 1 if l else 0

n, m = map(int ,input().split())

arr = sorted(list(map(int, input().split())))

part = list(map(int, input().split()))

answer = []
for p in part:
    count = bs_right(0, n-1, p)
    
    k = bs_right2(0, 300000, count)

    answer.append(k)
print(*answer)
