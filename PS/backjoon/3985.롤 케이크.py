import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

l = int(input())
n = int(input())

cakes = [-1] * l

part = [0] * n
ex = [0] * n

for i in range(n):
    p, k = map(int, input().split())
    
    ex[i] = k-p+1

    count = 0
    for j in range(p-1, k):
        if cakes[j] == -1:
            cakes[j] = i
            count += 1
    part[i] = count

mp = max(part)
mx = max(ex)

for i in range(n):
    if ex[i] == mx:
        print(i+1)
        break

for i in range(n):
    if part[i] == mp:
        print(i+1)
        break