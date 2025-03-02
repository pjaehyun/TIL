import sys
input = sys.stdin.readline

def kaprekar(s):

    res = 0
    while s != "6174":
        _max = sorted(s, reverse=True)
        _min = sorted(s)
        temp = str(int(''.join(_max)) - int(''.join(_min)))
        s = (4 - len(temp)) * '0' + temp
        res += 1
    return res

t = int(input())

for _ in range(t):
    num = input().strip()
    print(kaprekar(num))