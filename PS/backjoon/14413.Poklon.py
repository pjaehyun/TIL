import sys
from collections import defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
sqrt = n**0.5

nums = list(map(int, input().split()))

quries = []

for i in range(q):
    l, r = map(int, input().split())
    quries.append((l-1, r-1, i))

quries.sort(key=lambda x:(x[0]//sqrt, x[1]))
nums_count = defaultdict(int)

p_start, p_end, p_idx = quries[0]
answer = [0] * q
res = 0

def plus(x):
    global res
    if nums_count[x] == 2:
        res -= 1

    nums_count[x] += 1

    if nums_count[x] == 2:
        res += 1
    

def minus(x):
    global res
    if nums_count[x] == 2:
        res -= 1
    
    nums_count[x] -= 1

    if nums_count[x] == 2:
        res += 1

for i in range(p_start, p_end + 1):
    plus(nums[i])
answer[p_idx] = res

for i in range(1, q):
    start, end, idx = quries[i]

    while end > p_end:
        p_end += 1
        plus(nums[p_end])

    while end < p_end:
        minus(nums[p_end])
        p_end -= 1

    while start < p_start:
        p_start -= 1
        plus(nums[p_start])

    while start > p_start:
        minus(nums[p_start])
        p_start += 1

    answer[idx] = res

for a in answer:
    print(a)