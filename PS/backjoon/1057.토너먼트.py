import sys
import math
input = sys.stdin.readline

n, k, l = map(int, input().split())

if l < k:
    k, l = l, k

answer = 1

while k % 2 == 0 or k + 1 != l:
    answer += 1

    k = math.ceil(k / 2)
    l = math.ceil(l / 2)
print(answer)