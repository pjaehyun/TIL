import sys
input = sys.stdin.readline

T = int(input())

def distance(s1, s2):
    res = 0
    for i in range(4):
        if s1[i] != s2[i]:
            res += 1
    return res

for _ in range(T):
    n = int(input())
    lst = list(map(str, input().split()))
    answer = float('inf')

    if n > 32:
        print(0)
        continue
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                answer = min(answer, distance(lst[i], lst[j]) + distance(lst[i], lst[k]) + distance(lst[j], lst[k]))
    print(answer)