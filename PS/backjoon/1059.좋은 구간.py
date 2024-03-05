import sys
import math
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()
s = [0] + s
l += 1

start, end = 0, 1
answer = 0
while end < l:
    for i in range(s[start]+1, s[end]):
        for j in range(i+1, s[end]):
            if i <= n <= j:
                answer += 1
    start, end = start+1, end+1
print(answer)