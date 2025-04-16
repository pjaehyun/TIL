import sys
import decimal
input = sys.stdin.readline

x, y = map(int, input().split())

z = int(decimal.Decimal(y)/decimal.Decimal(x)*100)

l, r = 0, 1000000001

while l < r:
    mid = (l + r) // 2
    if int(decimal.Decimal(y+mid)/decimal.Decimal(x+mid)*100) <= z:
        l = mid + 1
    else:
        r = mid

if l == 1000000001:
    print(-1)
else:
    print(l)