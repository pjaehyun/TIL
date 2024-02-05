import sys
input = sys.stdin.readline

n, m = map(int, input().split())

prefix = list(map(int, input().split()))
s, e = 0, 1
answer = 0

while s <= e and e <= n:
    _sum = sum(prefix[s:e])
    if _sum == m:
        answer += 1
        e += 1
    elif _sum < m:
        e += 1
    else:
        s += 1
print(answer)