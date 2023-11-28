import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
sqrt = n**0.5

m = int(input())
queries = []

for i in range(m):
    s, e = map(int, input().split())
    queries.append((s-1, e-1, i))

queries.sort(key=lambda x:(x[0]//sqrt, x[1]))

def plus(x):
    global max_value
    if c_count[count[x]] != 0:
        c_count[count[x]] -= 1
    count[x] += 1
    c_count[count[x]] += 1
    max_value = max(max_value, count[x])

def minus(x):
    global max_value
    c_count[count[x]] -= 1
    if c_count[count[x]] == 0 and count[x] == max_value:
        max_value -= 1
    count[x] -= 1
    c_count[count[x]] += 1

answer = [0] * m
max_value = 0
c_count = [0] * 101010
count = [0] * 101010

c_count[0] = n

p_start, p_end, p_idx = queries[0]

for i in range(p_start, p_end + 1):
    plus(nums[i])


answer[p_idx] = max_value


for i in range(1, m):
    start, end, idx = queries[i]

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

    answer[idx] = max_value

for a in answer:
    print(a)