import sys
input = sys.stdin.readline

def bs(l, r, x):
    while l < r:
        mid = (l + r) // 2

        if coor[mid][0] < x:
            l = mid + 1
        else:
            r = mid
    return l

n = int(input())

coor = [list(map(int, input().split())) for _ in range(n)]

q = int(input())

for _ in range(q):
    k = float(input())

    idx = bs(0, n-1, k)
    
    if coor[idx][1] > coor[idx-1][1]:
        print(1)
    elif coor[idx][1] < coor[idx-1][1]:
        print(-1)
    else:
        print(0)