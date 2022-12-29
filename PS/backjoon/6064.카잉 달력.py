import math
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    find = False

    while x <= M*N:
        if (x-y) % N == 0:
            print(x)
            find = True
            break
        x += M
    if not find:
        print(-1)
    