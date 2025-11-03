import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

r, c, w = map(int, input().split())

p = [[0]*(i+2) for i in range(1,32)]

p[0][1] = 1

for i in range(1, 31):
    for j in range(1, i+2):
        p[i][j] = p[i-1][j] + p[i-1][j-1]

answer = 0
for i in range(w):
    for j in range(i+1):
        answer += p[i+r-1][c+j]
print(answer)
