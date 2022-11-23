import sys
input = sys.stdin.readline

eratos = [x for x in range(10000 + 1)]
# 에라토스테네스 
for i in range(2, int(10000 ** (1/2) + 1)):
    if eratos[i] != -1:
        j = 2
        while i * j <= 10000:
            eratos[i*j] = -1
            j += 1

N = int(input())
for _ in range(N):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if eratos[n - i] != -1 and eratos[i] != -1:
            print(i, n-i)
            break
