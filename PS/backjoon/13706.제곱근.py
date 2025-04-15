import sys
input = sys.stdin.readline

n = int(input())

l, r = 0, n

while l < r:
    mid = (l + r) // 2
    if mid**2 == n:
        l = mid
        break
    if mid**2 < n:
        l = mid + 1
    else:
        r = mid - 1
print(l)
