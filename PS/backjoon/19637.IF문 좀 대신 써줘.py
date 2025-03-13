import sys
input = sys.stdin.readline

def bs(l, r, x):
    while l < r:
        mid = (l + r) // 2

        if power[mid][0] < x:
            l = mid + 1
        else:
            r = mid
    return l

n, m = map(int, input().split())

power = []
is_power = set()
for _ in range(n):
    a, b = map(str, input().strip().split())
    
    if b in is_power: continue
    is_power.add(b)
    power.append((int(b), a))
power.sort(key=lambda x:(x[0], x[1]))

for _ in range(m):
    x = int(input())
    temp = bs(0, len(power) - 1, x)
    print(power[temp][1])