import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
sqrt = n**0.5

query = []

for i in range(m):
    s, e = map(int, input().split())
    query.append((s-1, e-1, i))

query.sort(key=lambda x:(x[0]//sqrt,x[1]))

answer = [0] * m

cache = defaultdict(int)
p_start, p_end, p_idx = query[0]

for i in range(p_start, p_end + 1):
    cache[arr[i]] += 1
answer[p_idx] = len(cache)

for i in range(1, m):
    s, e, idx = query[i]

    while e > p_end:
        p_end += 1
        cache[arr[p_end]] += 1
    while e < p_end:
        cache[arr[p_end]] -= 1
        if cache[arr[p_end]] == 0:
            del cache[arr[p_end]]
        p_end -= 1
    while s < p_start:
        p_start -= 1
        cache[arr[p_start]] += 1
    while s > p_start:
        cache[arr[p_start]] -= 1
        if cache[arr[p_start]] == 0:
            del cache[arr[p_start]]
        p_start += 1
    answer[idx] = len(cache)

for a in answer:
    print(a)
