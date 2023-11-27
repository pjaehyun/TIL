import sys
from collections import defaultdict
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))
sqrt = n**0.5

quries = []

for i in range(t):
    l, r = map(int, input().split())
    quries.append((l-1, r-1, i))

quries.sort(key=lambda x:(x[0]//sqrt, x[1]))
nums_count = defaultdict(int)

def plus(x):
    global res
    res -= (nums_count[x]**2*x)
    nums_count[x] += 1
    res += (nums_count[x]**2*x)


def minus(x):
    global res
    res -= (nums_count[x]**2*x)
    nums_count[x] -= 1
    res += (nums_count[x]**2*x)
    

answer = [0] * t

p_s, p_e, p_i = quries[0]
res = 0

for i in range(p_s, p_e+1):
    plus(arr[i])
answer[p_i] = res


for i in range(1, t):
    s, e, idx = quries[i]

    while p_e < e:
        p_e += 1
        plus(arr[p_e])

    while p_e > e:
        minus(arr[p_e])
        p_e -= 1

    while p_s > s:
        p_s -= 1
        plus(arr[p_s])

    while p_s < s:
        minus(arr[p_s])
        p_s += 1
    answer[idx] = res

for a in answer:
    print(a)
