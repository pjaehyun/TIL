import sys
input = sys.stdin.readline

n = int(input())

am, aw = map(int, input().split())
bm, bw = map(int, input().split())
cm, cw = map(int, input().split())

check = True

for i in range(am+1):
    a = i
    d = am - a
    e = cw - d
    b = bm - e
    c = aw - b
    f = cm - c

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        check = False
        break
if check:
    print(0)