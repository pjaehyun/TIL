import sys
input = sys.stdin.readline

def bs(x):
    l, r = 1, x

    while l <= r:
        mid = (l + r) // 2
        
        s = ((mid + 1) * mid) // 2

        if s < x:
            l = mid + 1
        else:
            r = mid - 1
    return l

t = int(input())

for _ in range(t):
    n = int(input())
    
    a = bs(n)
    
    if ((a + 1) * a) // 2 > n:
        print(a - 1)
    else: print(a)