import sys
input = sys.stdin.readline

N = 123456 * 2

primes = [x for x in range(N + 1)]

# 에라토스테네스의 체
for i in range(2, int(N ** (1/2) + 1)):
    if primes[i] != -1:
        j = 2
        while i * j <= N:
            primes[i*j] = -1
            j += 1
        
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, n*2+1):
        if primes[i] > 0:
            count += 1
    print(count)