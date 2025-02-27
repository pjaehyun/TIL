import sys
input = sys.stdin.readline

n, l = map(int, input().split())

time = 0
step = 0

for _ in range(n):
    d, r, g = map(int, input().split())
    time += d - step
    step = d
    if time % (r+g) <= r:
        time += r - time % (r+g)
time += l - step
print(time)