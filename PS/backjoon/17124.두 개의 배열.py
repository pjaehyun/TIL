import sys
input = sys.stdin.readline

def bs_left(l, r, x):
    while l < r:
        mid = (l + r) // 2
        if b[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = [-float('inf')] + sorted(list(map(int, input().split()))) + [float('inf')]

    answer = 0
    for e in a:
        idx = bs_left(0, m+1, e)
        l, r = idx - 1, idx

        if abs(e - b[l]) <= abs(e - b[r]):
            answer += b[l]
        else:
            answer += b[r]
    print(answer)