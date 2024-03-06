import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]
m = len(lst[0])
k = m
for i in range(m):
    dup = set()
    is_dup = False
    for j in range(n):
        if lst[j][::-1][:i+1][::-1] in dup:
            is_dup = True
            break
        dup.add(lst[j][::-1][:i+1][::-1])
    if not is_dup:
        k = min(k, i+1)
print(k)