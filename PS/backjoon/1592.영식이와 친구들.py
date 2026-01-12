import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n, m, l = map(int, input().split())

count = [0] * (n+1)
curr = 1

answer = 0
while True:
    if count[curr] % 2 == 0:
        curr = (curr + l) % n
    else:
        curr = (curr - l) % n

    count[curr] += 1

    if count[curr] == m:
        break
    
    answer += 1
print(answer)