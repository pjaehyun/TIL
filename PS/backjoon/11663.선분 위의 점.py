import sys
input = sys.stdin.readline

def bs(l,r,arr,x):
    while l < r:
        mid = (l + r) // 2

        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for _ in range(m):
    a, b = map(int, input().split())

    if a > arr[-1]: 
        print(0)
        continue
    i1 = bs(0, n-1, arr, a)
    i2 = bs(0, n-1, arr, b)
    
    if arr[i1] < a:
        i1 -= 1
    if arr[i2] > b:
        i2 -= 1
    print(i2 - i1 + 1)