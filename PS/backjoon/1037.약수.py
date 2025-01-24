import sys
input = sys.stdin.readline

n = int(input())
fac = list(map(int, input().split()))

print(min(fac) * max(fac))