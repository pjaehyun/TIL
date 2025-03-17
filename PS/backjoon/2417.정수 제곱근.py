import sys
input = sys.stdin.readline

n = int(input())

l, r = 0, 2**32+1

while l < r:
    mid = (l + r) // 2

    if mid**2 < n:
        l = mid + 1
    else:
        r = mid
print(l)