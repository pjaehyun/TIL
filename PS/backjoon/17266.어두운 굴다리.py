import sys
input = sys.stdin.readline

def light(h):
    l, r = 0, 0

    for i in range(len(arr)):
        if r >= arr[i] - h:
            r = arr[i] + h
        else:
            return False
    if r < n: return False
    return True
        

n = int(input())

m = int(input())

arr = list(map(int, input().split()))

l, r = 0, n

while l < r:
    mid = (l + r) // 2
    if not light(mid):
        l = mid + 1
    else:
        r = mid
print(l)
