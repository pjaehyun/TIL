import sys
input = sys.stdin.readline

n = int(input())

l, r = 1, 10000000001

while l < r:
    mid = (l + r) // 2

    if (mid*3)*(mid-1)+1 < n:
        l = mid + 1
    else:
        r = mid
print(l)