import sys
import math
input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))

m = int(input())

for _ in range(m):
    s, num = map(int, input().split())

    if s == 1:
        for i in range(num, n+1, num):
            switch[i] ^= 1
    else:
        switch[num] ^= 1
        l, r = num-1, num+1
        while (l >= 1 and r <= n) and (switch[l] == switch[r]):
            switch[l] ^= 1
            switch[r] ^= 1
            l -= 1
            r += 1
switch = switch[1:]
answer = [switch[n // 20 * 20:n//20*20+20]]
for a in answer:
    print(*a)