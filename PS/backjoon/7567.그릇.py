import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

s = input().strip()

answer = 10
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        answer += 10
    else:
        answer += 5
print(answer)