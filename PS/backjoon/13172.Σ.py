import sys
import math
input = sys.stdin.readline

N = int(input())
mod = 1000000007

def pow(x, n):
    if n == 1:
        return x % mod
    if n % 2 == 0:
        temp = pow(x, n // 2)
        return (temp * temp) % mod
    else:
        return x*pow(x, n-1)%mod
    
answer = 0
for _ in range(N):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd
    answer += s*pow(n, mod-2) % mod
    answer %= mod
print(answer)