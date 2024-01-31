import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
packages = []
singles = []

for _ in range(m):
    p, s = map(int, input().split())
    packages.append(p)
    singles.append(s)

packages.sort()
singles.sort()

print(min(math.ceil(n/6) * packages[0], n * singles[0], n // 6 * packages[0] + (n % 6 * singles[0])))