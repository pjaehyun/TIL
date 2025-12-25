import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, k = map(int, input().split())

s = list(map(int, input().split()))

d = list(map(int, input().split()))


for _ in range(k):
    temp = [0] * n
    for i in range(n):
        temp[d[i]-1] = s[i]
    s = temp
print(*s)