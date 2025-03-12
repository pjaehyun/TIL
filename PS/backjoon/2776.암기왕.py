import sys
input = sys.stdin.readline

def bs(l, r, x):
    
    while l < r:
        mid = (l + r) // 2
        
        if note1[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

t = int(input())

for _ in range(t):
    n = int(input())
    note1 = sorted(list(map(int, input().split())))

    m = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        if note1[bs(0, n-1, num)] == num:
            print(1)
        else:
            print(0)
        
